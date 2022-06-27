import socket               # Import socket module
import random,os,time
i=0
while i == 0:
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 1245 
    s.connect((host, port))
    msg = (str)(random.randint(1,6))

    s.send(msg.encode("utf-8"))
    i = s.recv(1024).decode('utf-8')
    i = int(i)
    time.sleep(0.001)
    s.close()
