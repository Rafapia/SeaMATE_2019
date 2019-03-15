from SocketUtils.SocketUtils import ClientSocket
from socket import error as socketError
from time import sleep
import threading
import cv2


	


# Run script.
if (__name__=='__main__'):

	# Create objects.
	client = ClientSocket(verbose=0)
	camera = cv2.VideoCapture(0)

	# Set maximum FPS.
	FPS = 20

	# Calculate the frame interval.
	frameInterval = 1/FPS

	# Always try to connect to server and stream data.
	while True:

		# If any error occurs, try again.
		try:

			# Setup the Client socket for streaming.
			client.initSocket()
			client.connect('localhost', 5555)

			# Once the connection is established, send video stream.
			while True:

				# Grab frame.
				ret, frame = camera.read()

				# Shrink frame's size.
				# frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
				frame = cv2.resize(frame, (800, 500))

				# Encode frame
				encoded, frame = cv2.imencode(".jpg", frame)

				# Send frame to Server.
				client.send(frame)


				# Receive commands from the Server.
				command = client.recv()
				if (command=="Kill Client"):
					# Close everything properly.
					client.close()
					camera.release()
					
					
					# End print.
					print("Client closed.")

					# Close program.
					exit()


				print(command)

				# Wait interval for max FPS to be achieved.
				sleep(frameInterval)


		except Exception as e:

			# If connection refused, try again.
			print(f"Trying to connect with server.")
			sleep(1)



	
