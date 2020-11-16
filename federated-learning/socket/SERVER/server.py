import socket
import pickle
import server_utils as su
from mlsocket import MLSocket
import socket

s = MLSocket()
#s = socket.socket()
s.bind(("192.168.1.103", 10000))
s.listen(1)
print("Listening for connections...")
conn, addr = s.accept()

print('Connected by', addr)
filename = "model.json"
file =  open(filename, 'rb')
sendfile = file.read()
conn.sendall(sendfile)
    
file.close()
print("Model sent to the client")


data = conn.recv(3000000)
print("Received weights from client: ")
weights_file = "weights.h5"
# with soc,open(weights_file,'wb') as file2:
#file2 = open(weights_file,'wb')
#file2.write(data)

print("weights have been received.")
print("Evaluation of the model...")
su.load_weights_and_evaluate(data)


print("socket closed")
s.close()
   
