import socket
import pickle
import SERVER.server_utils as su

from mlsocket import MLSocket
import socket

soc = MLSocket()
#soc = socket.socket()
print("Socket is created.")

#Raspberry IP
soc.connect(("192.168.1.103", 10000))
print("Connected to the server.")

savefilename = "model.json"
file = open(savefilename,'wb') 
recvfile = soc.recv(4096)
file.write(recvfile)
file.close()
print("Model received.")

print("Training model with local data...")
model = su.load_model_and_train()
print("Model trained.")
print("sending weights to server...")


filename = "weights.h5"
file =  open(filename, 'rb')
sendfile = file.read()
#soc.send(sendfile)
soc.send(model)
print("weights sent")
#print("Socket is closed.")
#soc.close()

