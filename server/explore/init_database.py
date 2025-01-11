from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, Document

from postgres import get_postgres_connection, get_storage_context

# take environment variables from .env
load_dotenv() 

# initialize the database with a dummy document
doc = Document(text="init", doc_id="init")
VectorStoreIndex.from_documents([doc], storage_context=get_storage_context(), show_progress=True)

# truncate the tables - the above command is supposed to do this, but it doesn't
conn = get_postgres_connection()
conn.execute("truncate table public.data_documents")
conn.execute("truncate table public.data_chunks")