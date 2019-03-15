'''
    Author: Rafael Piacsek
    Date: Mar 13, 2019.

    This class serves as an abstraction layer for handling Server and Client sockets for
    sending pickled objects from one to another.
'''

import socket
import pickle



class ServerSocket:
    '''
    This class hanldes all the work from a Server socket.
    '''


    def __init__(self, ip, port, bufferSize=4096, headerSize=10, maxClients=1, verbose=1):
        '''
        Constructor method. Creates the Server socket and stores all necessary variables.
        :param ip: The Server IP.
        :param port: The Port to be used.
        :param bufferSize: Buffer size. Should match the client's buffer size.
        :param headerSize: Message header's size. Should match client's header size.
        :param maxClients: Maximum number of clients to connect at once.
        :param verbose: Whether to be verbose on operations or not.
        '''

        # Store all field variables.
        self.IP = ip
        self.PORT = port
        self.ADDRESS = (self.IP, self.PORT)
        self.BUFFER_SIZE = bufferSize
        self.HEADER_SIZE = headerSize
        self.MAX_CLIENTS = maxClients
        self.VERBOSE = verbose




    def initSocket(self):
        '''
        This method sets up the socket.
        :return:
        '''
        try:
            # Checkpoint print.
            if (self.VERBOSE==2):
                print(f"Creating Server socket at {self.ADDRESS}")

            # Create Server socket.
            self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Checkpoint print.
            if (self.VERBOSE==1):
                print(f"Successfuly created Server socket at {self.ADDRESS}")

        except Exception as e:
            raise Exception(e)


        try:
            # Checkpoint print.
            if (self.VERBOSE==2):
                print(f"Binding Server socket at {self.ADDRESS}")

            # Create Server socket.
            self.SOCKET.bind(self.ADDRESS)

            # Checkpoint print.
            if (self.VERBOSE==1):
                print(f"Successfuly bound Server socket at {self.ADDRESS}")

        except Exception as e:
            raise Exception(e)

        try:
            # Checkpoint print:
            if (self.VERBOSE==1):
                print(f"Server socket listening to port {self.PORT}")

            # Socket listen.
            self.SOCKET.listen(self.MAX_CLIENTS)

        except Exception as e:
            raise Exception(e)




    def acceptConnections(self):
        '''
        Accepts socket connection requests.
        :return:
        '''

        # Accept connection.
        self.CLIENT, self.CLIENT_ADDRESS = self.SOCKET.accept()

        # Checkpoint print.
        if (self.VERBOSE==1):
            print(f"Connected with {self.CLIENT_ADDRESS}")




    def send(self, data):
        '''
        Sends any object to the connected socket.
        :param data: The object to be sent.
        :return:
        '''

        # Check if there is client to send data.
        if (self.CLIENT is None):
            raise Exception("No client to send data to.")

        # Prepare data for tranfer.
        data = self.packData(data)

        # Send data to Client.
        self.CLIENT.sendall(data)




    def recv(self):
        '''
        Receives serialized data from another socket, recontructs the data, and
        returns the object that was originally sent.
        :return: The object received.
        '''

        # Variable to hold data.
        data = b''

        # Flag to check if block contains header.
        newIncoming = True

        while True:

            # Recieve the block of data from the client.
            incoming = self.CLIENT.recv(self.BUFFER_SIZE)

            # If it's the first block, get header.
            if (newIncoming):
                # Get header value.
                incomingLen = int(incoming[:self.HEADER_SIZE])
                # Set flag to false.
                newIncoming = False

            # Append new data to other data.
            data += incoming

            # If all data is received, end loop.
            if (len(data)-self.HEADER_SIZE == incomingLen):
                # Break out of loop.
                break

        # Unpack data.
        data = self.unpackData(data)

        # Return received data.
        return data



    def close(self):
        '''
        This method closes the Server socket for connections.
        :return:
        '''

        # Checkpoint print.
        if (self.VERBOSE==2):
            print(f"Closing Server socket at {self.ADDRESS}")

        # Close socket.
        self.SOCKET.close()

        # Checkpoint print.
        if (self.VERBOSE==1):
            print(f"Closed Server socket at {self.ADDRESS}")



    def packData(self, data):
        '''
        Given any object, this method serializes the data and adds the header.
        :param data: The object to be packed.
        :return: The processed data.
        '''

        # Serialize the data.
        data = pickle.dumps(data)

        # Add header to the beginning of serialized data.
        data = bytes(f"{len(data):<{self.HEADER_SIZE}}", "utf-8") + data

        # Return packed data.
        return data




    def unpackData(self, data):
        '''
        Given a serialized data, it removes the header and returns the original object
        :param data: The serialized data to be unpacked.
        :return:
        '''

        # Remove header.
        dataLen = int(data[:self.HEADER_SIZE])
        data = data[self.HEADER_SIZE:]

        # Unserialize data.
        data = pickle.loads(data)

        return data



    def __str__(self):
        '''
        To String method. Retuns the basic information of this Server socket.
        :return: The basic information of this Server socket.
        '''

        str = f"Server socket bound to {self.ADDRESS}"

        # Return the String
        return str





class ClientSocket:


    def __init__(self,bufferSize=4096, headerSize=10, verbose=1):

        # Store field variables.
        self.BUFFER_SIZE = bufferSize
        self.HEADER_SIZE = headerSize
        self.VERBOSE = verbose



    def initSocket(self):
        '''
        This method initializes the socket with the given specifications.
        :return:
        '''

        try:
            # Checkpoint print.
            if (self.VERBOSE==2):
                print(f"Creating Client TCP/STREAM socket.")

            # Create Server socket.
            self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Checkpoint print.
            if (self.VERBOSE==1):
                print(f"Successfuly created Client TCP/STREAM socket.")

        except Exception as e:
            raise Exception(e)



    def connect(self, ip, port):
        '''
        This method connects the Client socket to the desired server address.
        :param ip: The Server's IP address.
        :param port: The Server's port.
        :return:
        '''

        # Store Server Address.
        self.SERVER_IP = ip
        self.SERVER_PORT = port
        self.SERVER_ADDRESS = (self.SERVER_IP, self.SERVER_PORT)


        try:
            # Checkpoint print.
            if (self.VERBOSE==2):
                print(f"Connecting Client to Server at {self.SERVER_ADDRESS}.")

            # Create Server socket.
            self.SOCKET.connect(self.SERVER_ADDRESS)

            # Checkpoint print.
            if (self.VERBOSE==1):
                print(f"Successfuly created Client TCP/STREAM socket.")

        except Exception as e:
            raise Exception(e)



    def send(self, data):
        '''
        This method sends any data to the connected Server.
        :param data: Any object to be sent.
        :return:
        '''

        # Check if there is client to send data.
        if (self.SOCKET is None):
            raise Exception("No client to send data to.")

        # Prepare data for tranfer.
        data = self.packData(data)

        # Send data to Client.
        self.SOCKET.sendall(data)



    def recv(self):
        '''
        This method receives all data, deals with buffering, and returns the received object.
        :return: The object sent by the other end.
        '''

        # Variable to hold data.
        data = b''

        # Flag to check if block contains header.
        newIncoming = True

        while True:

            # Recieve the block of data from the client.
            incoming = self.SOCKET.recv(self.BUFFER_SIZE)

            # If it's the first block, get header.
            if (newIncoming):
                # Get header value.
                incomingLen = int(incoming[:self.HEADER_SIZE])
                # Set flag to false.
                newIncoming = False

            # Append new data to other data.
            data += incoming

            # If all data is received, end loop.
            if (len(data) - self.HEADER_SIZE == incomingLen):
                # Break out of loop.
                break

        # Unpack data.
        data = self.unpackData(data)

        # Return received data.
        return data



    def packData(self, data):
        '''
        Given any object, this method serializes the data and adds the header.
        :param data: The object to be packed.
        :return: The processed data.
        '''

        # Serialize the data.
        data = pickle.dumps(data)

        # Add header to the beginning of serialized data.
        data = bytes(f"{len(data):<{self.HEADER_SIZE}}", "utf-8") + data

        # Return packed data.
        return data



    def unpackData(self, data):
        '''
        Given a serialized data, it removes the header and returns the original object
        :param data: The serialized data to be unpacked.
        :return:
        '''

        # Remove header.
        dataLen = int(data[:self.HEADER_SIZE])
        data = data[self.HEADER_SIZE:]

        # Unserialize data.
        data = pickle.loads(data)

        return data



    def close(self):
        '''
        This method closes the Client socket.
        :return:
        '''

        # Checkpoint print.
        if (self.VERBOSE == 2):
            print(f"Closing Client socket.")

        # Close socket.
        self.SOCKET.close()

        # Checkpoint print.
        if (self.VERBOSE == 1):
            print(f"Closed Client socket.")



    def __str__(self):
        '''
        To String method. Retuns the basic information of this Server socket.
        :return: The basic information of this Server socket.
        '''

        str = f"Client socket connected to {self.SERVER_ADDRESS}"

        # Return the String
        return str