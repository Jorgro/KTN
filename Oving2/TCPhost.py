from socket import *
import sys



#Create TCP/IP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind the socket to the port
print(gethostbyname(gethostname()))
server_address = ('', 10002)
serverSocket.bind(server_address)

#listen for incoming connections
serverSocket.listen(1)

htmlheader = "HTTP/1.0 200 OK\n" + "Content-Type: text/html\n\n"

while True:
    #wait for a connection

    print("Waiting for connection")
    connection, client_address = serverSocket.accept()

    try:
        message = connection.recv(1024).decode()

        filepath = message.split()[1]

        print(filepath)
        f = open("/Users/jorgenrosager/Library/Mobile Documents/com~apple~CloudDocs/KTN/Oving2" + filepath)

        outputdata = f.read()
        print("Sending back data")
        
        connection.send(htmlheader.encode())

        response = outputdata + "\r\n"
        connection.send(response.encode())
        connection.close()
    except (IOError, IndexError):
        connection.send(htmlheader.encode())
        connection.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())


