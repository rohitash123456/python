import socket               # Import socket module
var=1
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 2235                # Reserve a port for your service.

s.connect((host, port))
while var==1:
 print s.recv(1024)
 str=raw_input("enter msg here:")
 s.send(str)
s.close  
