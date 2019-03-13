import socket
import json
import numpy as np


SERVER_IP = 'localhost'
SERVER_PORT = 5555
MAX_NUM_CONNECTIONS = 1
BUFFER_SIZE = 1024


if __name__=='__main__':


	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((SERVER_IP, SERVER_PORT))
	server.listen(MAX_NUM_CONNECTIONS)
	print("Server running...")

	connection, address = server.accept()
	print(f"Connection established to address {address}")

	while True:

		data = connection.recv(BUFFER_SIZE)
		data = data.decode("utf-8")

		if (data is None):
			break

		print(f"Received data: {data}")

		connection.send(f"Received data: {data}".encode("utf-8"))


  	# connection.close()
