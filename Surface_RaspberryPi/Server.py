from SocketUtils.SocketUtils import ServerSocket
import threading
import cv2



# Run
if (__name__=='__main__'):

	# Create all objects.
	server = ServerSocket('localhost', 5555)

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


	except Exception as e:

		# print(e)
		server.send("Kill Client")
		server.close()
		cv2.destroyAllWindows()
		print("Server closed.")
