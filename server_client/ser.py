#!/usr/bin/python

import socket               # Import socket module
import sys
import select
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9999                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   while True:
	  str=c.recv(10)
	  print str
c.close()               
