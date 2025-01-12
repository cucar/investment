from postgres import index_document

# load edited analysis file and read its content
file = open("./analysis.txt") 
analysis = file.read()
file.close()

# index the edited analysis in the database
index_document(analysis)