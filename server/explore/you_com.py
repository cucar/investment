import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from typing import Dict, List, Union, Optional

load_dotenv()

def fetch_webpage_content(url: str) -> Optional[str]:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None

def call_you_com_api(endpoint: str, method: str, query: str, count: int = 2) -> Dict:
    """Make a raw API call to You.com"""
    if endpoint == "research":
        base_url = "https://chat-api.you.com"
    else:
        base_url = "https://api.ydc-index.io"

    url = f"{base_url}/{endpoint}"
    headers = {"X-API-Key": os.environ['YOUCOM_API_KEY']}
    payload = {"query": query, "count": count}

    if method == "GET":
        response = requests.request(method, url, params=payload, headers=headers)
    else:
        response = requests.request(method, url, json=payload, headers=headers)

    return response.json()

def process_news_results(data: Dict) -> List[Dict]:
    """Process news API response"""
    results = data['news']['results']
    for result in results:
        content = fetch_webpage_content(result['url'])
        result['webpage_content'] = content if content else ''
    return results

def process_search_results(data: Dict) -> List[Dict]:
    """Process search API response"""
    results = data['hits']
    for result in results:
        content = fetch_webpage_content(result['url'])
        result['webpage_content'] = content if content else ''
    return results

def process_research_results(data: Dict) -> Dict:
    """Process research API response"""
    search_results = data.get('search_results', [])
    for result in search_results:
        content = fetch_webpage_content(result['url'])
        result['webpage_content'] = content if content else ''
    
    return {
        'answer': data.get('answer', ''),
        'search_results': search_results
    }

def call_you_com(query: str, count: int = 2, endpoint: str = "news") -> Union[List[Dict], Dict]:
    """
    Call You.com API and process results based on endpoint
    
    Args:
        query: Search query string
        count: Number of results (for news endpoint)
        endpoint: API endpoint ('news', 'search', or 'research')
    
    Returns:
        For news: List of news articles with webpage content
        For search: List of search results with webpage content
        For research: Dict with answer and search results with webpage content
    """
    method = "POST" if endpoint in ["research"] else "GET"
    data = call_you_com_api(endpoint, method, query, count)
    
    if endpoint == "news":
        return process_news_results(data)
    elif endpoint == "search":
        return process_search_results(data)
    elif endpoint == "research":
        return process_research_results(data)
    else:
        raise ValueError(f"Unsupported endpoint: {endpoint}")
