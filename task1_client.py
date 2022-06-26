import socket               # Import socket module
import random,os,time
for i in range(4000):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 1245 
    s.connect((host, port))
    msg = (str)(random.randint(1,6))

    s.send(msg.encode("utf-8"))
    time.sleep(0.001)
    s.close()
