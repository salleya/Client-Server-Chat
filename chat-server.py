####################################################################################
# Amy Salley
# CS 372
# 10 March 2022
# 
# Program modified from class textbook "Computer Networking, A Top-Down Approach"
# by Kurose and Ross Section 2.7.2 Socket Programming with TCP TCPServer.py
#
# and Socket Programming in Python (Guide) https://realpython.com/python-sockets/
#
####################################################################################

# Import python socket API
from socket import *

# Assign port number
serverHost = "localhost"
serverPort = 3000

# Create the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Set the socket reuse option
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

with serverSocket:

    # Bind to 'localhost' and port 3000
    serverSocket.bind((serverHost, serverPort))

    # Listen for a client connection request
    serverSocket.listen()
    print("Server listening on:", serverHost, "on port:", serverPort)

    # Accept the connection between the client and server
    connectionSocket, addr = serverSocket.accept()

    with connectionSocket:
        print(f"Connected by {addr}")
        print('Waiting for message...')
        
        # Receive data from socket request
        received = connectionSocket.recv(1024)
            
        # Display the message from the client
        print(received.decode())

        # Display instructions for server user
        print('Type /q to quit')
        print('Enter message to send...')

        # Initialize a message to send to the client
        message = ""

        # Continue until the server user enters '/q' to quit
        while message != "/q":

            # Prompt server user for reply
            message = input("> ")

            # Send the message to the client
            if message != "/q":
                connectionSocket.sendall(message.encode())
            
                # Receive data from socket request
                received = connectionSocket.recv(1024)

                # End if client user has quit
                if not received:
                    break
            
                # Display the message from the client
                print(received.decode())

# Close the connection socket
connectionSocket.close()
