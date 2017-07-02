"""#from xml.extree import ElementTree
import gdata.docs.service
client=gdata.docs.service.DocsService()
client.ClientLogin("rohitashkumar781@gmail.com",'9001002118')
documents_feed=client.GetDocumentListFeed()
for document_entry in documents_feed.entry:
	print(document_entry.title.text)"""


import gdata.docs.service

# Create a client class which will make HTTP requests with Google Docs server.
client = gdata.docs.service.DocsService()
# Authenticate using your Google Docs email address and password.
#client.ClientLogin('jo@gmail.com', 'password')

client.ClientLogin('rohitashkumar781@gmail.com','9001002118')
# Query the server for an Atom feed containing a list of your documents.
documents_feed = client.GetDocumentListFeed()
# Loop through the feed and extract each document entry.
for document_entry in documents_feed.entry:
  # Display the title of the document on the command line.
  print document_entry.title.text

