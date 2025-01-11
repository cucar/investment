import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, Document
from llama_index.vector_stores.postgres import PGVectorStore

# take environment variables from .env
load_dotenv() 

# setup vector store with postgres
vector_store = PGVectorStore.from_params(
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
        "hnsw_dist_method": "vector_cosine_ops",
    },
)

# setup storage context with postgres vector store
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# load sample text from file and create a document object
file = open("./paul_graham.txt") 
file_text = file.read()
doc = Document(text=file_text)
file.close()

# create index from the document
index = VectorStoreIndex.from_documents([ doc ], storage_context=storage_context, show_progress=True)