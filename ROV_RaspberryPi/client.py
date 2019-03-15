from SocketUtils.SocketUtils import ClientSocket
from time import sleep
import cv2


# Create objects.
client = ClientSocket(verbose=0)
camera = cv2.VideoCapture(0)

# Set FPS.
FPS = 20
frameInterval = 1/FPS


# REMOVE THIS BREAK METHOD FOR REAL ROBOT!!
# OTHERWISE THE ROBOT WILL HAVE TO BE REBOOTED 
# TO REINITIALIZE THE CLIENT.
# Handle KeyboardInterrupts. 
try:

    # Always try to connect to server and stream data.
    while True:

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
            	raise KeyboardInterrupts

            print(command)

            # Wait interval for max FPS to be achieved.
            sleep(frameInterval)


except Exception:
    client.close()
    camera.release()


# End print.
print("Client closed.")