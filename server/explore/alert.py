from you_com import call_you_com
from postgres import index_document

# this is to emulate the alert system - user will receive an alert if the the found news is not already in the database
# call you.com api to get the latest news regarding the project alert and save them to the database if not already there 
alert = "housing turnover rates changing"
rows = call_you_com(alert, 10, "news")
for row in rows:
    
    # print the news for debug
    print(f"URL: {row['url']}")
    print(f"Title: {row['title']}")
    print(f"Description: {row['description']}")
    print(f"Age: {row['page_age']}")
    print("--------------------------------")
    print(row['webpage_content'])
    print("--------------------------------")

    # check if this news is already in the database - if not, save it and send an alert to the user
    # for now, we will just save it to the database without check or alert
    # conn = get_postgres_connection()
    # conn.execute("INSERT INTO projects_feed (feed_url, feed_title, feed_description, feed_time, feed_content) VALUES (%s, %s, %s, %s, %s)", (
    #     news['url'], news['title'], news['description'], news['page_age'], news['webpage_content']))
    # conn.close()
    index_document(row['webpage_content'])