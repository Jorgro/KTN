from socket import *


clientSocket = socket(AF_INET, SOCK_STREAM)
server_address = ('192.168.137.98', 10002)

print(f"connecting to {server_address[0]} port {server_address[1]}")

try:
    message = "Hello there, General Kenobi!"
    print("Sending message: ", message)
    clientSocket.sendall(message.encode())


    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("received ", data)
finally:
    print("closing socket")
    clientSocket.close()
