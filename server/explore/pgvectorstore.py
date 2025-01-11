import os
from dotenv import load_dotenv
from llama_index.core import StorageContext
from llama_index.storage.docstore.postgres import PostgresDocumentStore
from llama_index.vector_stores.postgres import PGVectorStore

# take environment variables from .env
load_dotenv() 

# returns the document store with postgres
def get_pg_document_store():
    return PostgresDocumentStore.from_params(
        host=os.environ['POSTGRES_HOST'],
        port=os.environ['POSTGRES_PORT'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        database=os.environ['POSTGRES_DATABASE'],
        table_name="documents"
    )


# returns the vector store with postgres
def get_pg_vector_store():
    return PGVectorStore.from_params(
        host=os.environ['POSTGRES_HOST'],
        port=os.environ['POSTGRES_PORT'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        database=os.environ['POSTGRES_DATABASE'],
        table_name="chunks",
        embed_dim=1536, # openai embedding dimension
        hnsw_kwargs={
            "hnsw_m": 16,
            "hnsw_ef_construction": 64,
            "hnsw_ef_search": 40,
            "hnsw_dist_method": "vector_cosine_ops"
        },
    )