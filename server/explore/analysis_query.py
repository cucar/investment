from postgres import get_vector_index

index = get_vector_index()

query_engine = index.as_query_engine(vector_store_query_mode="hybrid")

# This is to emulate user asking for consensus and orthogonal views after collecting more data
query = """what are the consensus and orthogonal views regarding the housing turnover rates in 2024? 
Please provide a summary of the views and the sources. Explain and discuss in detail."""
response = query_engine.query(query)
print(response)

# Write the response to analysis.txt - normally we would be saving this to the database as analysis result - more like a chat log
# but for now we will just save it to a file and change it manually and save it to the database in analysis_update.py
with open('analysis.txt', 'w') as f:
    f.write(str(response))
