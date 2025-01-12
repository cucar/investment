from postgres import get_vector_index

index = get_vector_index()

query_engine = index.as_query_engine(vector_store_query_mode="hybrid")

# This is to emulate user generating a memo based on the analysis
# this would be saved to the database as a memo object, to be used for copy-paste in UI
# just show the results for now
query = """You are an investment analyst, writing an investment newsletter. 
Write a paragraph with an investment thesis based on the analysis. 
Summarize the differing views with their reasons, and present them as intriguing perspectives.
Present a consensus and opposing view."""
response = query_engine.query(query)
print(response)