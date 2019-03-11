from socket import *


print(gethostbyname(gethostname()))

serverPort = 13213

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

print(serverSocket)

serverSocket.listen(1)

print('Ready')
while True:
    connectionSocket, addr = serverSocket.accept()
    print('connected')
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
