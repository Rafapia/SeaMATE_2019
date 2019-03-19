from SocketUtils.SocketUtils import ServerSocket, SocketUtilsException
import threading
import cv2
import time



# Run
if (__name__=='__main__'):

	# Create all objects.
	server = ServerSocket('192.168.86.92', 5555)

	# Setup Server socket.
	server.initSocket()

	# Command.
	command = "Kill Client."


	try:
		# Continously accept new connections.
		while True:

			# Checkpoint print.
			print("Waiting for connections.")

			# Accept new connection.
			server.acceptConnections()


			# Continuously get new frames from Client.
			while True:

				# Start.
				start = time.time()

				# Receive frame
				frame = server.recv()

				# Decode frame.
				frame = cv2.imdecode(frame, 1)

				# Show frame.
				cv2.imshow("Video Feed", frame)


				# Sent command to Client.
				server.send(command)

				# Check for close.
				if (cv2.waitKey(2) == 27):
					break

				print(f"FPS: {1/(time.time()-start)}")

	except SocketUtilsException as e:
		print("Socket Error")

	except Exception as e:

		# print(e)
		server.send("Kill Client")
		server.close()
		cv2.destroyAllWindows()
		print("Server closed.")
