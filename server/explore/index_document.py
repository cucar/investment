from llama_index.core import StorageContext, VectorStoreIndex, Document

from pgvectorstore import get_pg_document_store, get_pg_vector_store

# load sample text from file and create a document object
file = open("./paul_graham.txt") 
file_text = file.read()
doc = Document(text=file_text)
file.close()

# index the document
storage_context = StorageContext.from_defaults(docstore=get_pg_document_store(), vector_store=get_pg_vector_store())
index = VectorStoreIndex.from_documents([ doc ], storage_context=storage_context, show_progress=True)