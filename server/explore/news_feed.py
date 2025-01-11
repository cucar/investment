from you_com import call_you_com
from postgres import get_postgres_connection

conn = get_postgres_connection()

# add a news article to the projects feed - we will add original content and attributes to the database later
def save_news_document(news):
    conn.execute("INSERT INTO projects_feed (feed_url, feed_title, feed_description, feed_time, feed_content) VALUES (%s, %s, %s, %s, %s)", (
        news['url'], news['title'], news['description'], news['page_age'], news['webpage_content']))

# call you.com api to get the latest news regarding the project and save them to the database
rows = call_you_com("Housing market", 2)
for row in rows:
    
    # print the news for debug
    print(f"URL: {row['url']}")
    print(f"Title: {row['title']}")
    print(f"Description: {row['description']}")
    print(f"Age: {row['page_age']}")
    print("--------------------------------")
    print(row['webpage_content'])
    print("--------------------------------")

    # save the news to the database
    save_news_document(row)

conn.close()