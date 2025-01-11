from postgres import index_document

# load sample text from file and create a document object
file = open("./paul_graham.txt") 
file_text = file.read()
file.close()

# index the document in the existing database
index_document(file_text)