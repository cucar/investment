from postgres import get_vector_index

index = get_vector_index()

query_engine = index.as_query_engine(vector_store_query_mode="hybrid")

print(query_engine.query("What did the author do with 1401?"))