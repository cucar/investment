from llama_index.core import VectorStoreIndex

from pgvectorstore import get_pg_vector_store

index = VectorStoreIndex.from_vector_store(vector_store=get_pg_vector_store())

query_engine = index.as_query_engine()

print(query_engine.query("What did the author do?"))