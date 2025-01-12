from you_com import call_you_com
from postgres import index_document

# this is to emulate the user doing a research after receiving an alert
# call you.com api for research save them to the database if not already there 
topic = "Can you give me some information on the housing turnover rates in 2024 vs 2025? What are the predictions for 2025?"
rows = call_you_com(topic, 10, "search") # using search endpoint for now instead of research because it requires payment
for row in rows:
    
    # print the results for debug
    print(f"URL: {row['url']}")
    print(f"Title: {row['title']}")
    print(f"Description: {row['description']}")
    # print(f"Snippets: {row['snippets']}")
    print("--------------------------------")
    print(row['webpage_content'])
    print("--------------------------------")

    # check if this page is already in the database - if not, save it - it will be used for analysis
    index_document(row['webpage_content'])