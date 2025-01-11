import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# load you.com API key
load_dotenv()

def fetch_webpage_content(url):
    try:
        # Add User-Agent header to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text content
        text = soup.get_text()
        
        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None

def call_you_com(query, count):
    url = "https://api.ydc-index.io/news"
    headers = {"X-API-Key": os.environ['YOUCOM_API_KEY']}
    payload = {"query": query, "count": count}
    response = requests.request("GET", url, params=payload, headers=headers)
    data = response.json()
    results = data['news']['results']
    
    # Add webpage content to each result
    for result in results:
        content = fetch_webpage_content(result['url'])
        result['webpage_content'] = content if content else ''
    
    return results
