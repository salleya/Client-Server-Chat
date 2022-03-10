####################################################################################
# Amy Salley
# CS 372
# 10 March 2022
# 
# Program modified from class textbook "Computer Networking, A Top-Down Approach"
# by Kurose and Ross Section 2.7.2 Socket Programming with TCP TCPClient.py
#
# and Socket Programming in Python (Guide) https://realpython.com/python-sockets/
#
####################################################################################

# Import python socket API
from socket import *

# Define the socket connection host and port
serverName = 'localhost'
serverPort = 3000

# Create the client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

with clientSocket:

    # Connect to the server
    clientSocket.connect((serverName, serverPort))
    print("Connected to:", serverName, "on port:", serverPort)
    
    # Print instructions
    print("Type /q to quit")
    print("Enter message to send...")

    # Initialize a message to send to the server
    message = ""

    # Continue until the client user enters '/q' to quit
    while message != '/q':
        
        # Prompt client user for input
        message = input('> ')

        if message != "/q":

            # Send a message to the server
            clientSocket.sendall(message.encode())
        
            # Receive a response from the server
            serverResponse = clientSocket.recv(1024)

            # End if server user has quit
            if not serverResponse:
                break

            # Display the response from the server
            print(serverResponse.decode())

# Close the socket
clientSocket.close()
