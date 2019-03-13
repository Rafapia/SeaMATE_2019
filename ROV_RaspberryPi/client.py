import socket
import json
import numpy as np


CLIENT_IP = 'localhost'
CLIENT_PORT = 5555
MAX_NUM_CONNECTIONS = 1
BUFFER_SIZE = 1024
MESSAGE = "Hey! We have established a connection!"

if (__name__=='__main__'):

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((CLIENT_IP, CLIENT_PORT))
	client.send(MESSAGE.encode("utf-8"))
	
	data = client.recv(BUFFER_SIZE)
	data = data.decode("utf-8")
	client.close()
	
	print(f"received data: {data}")
