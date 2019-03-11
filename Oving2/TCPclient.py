from socket import *

serverName = '128.238.251.26'

serverPort = 10002
clientSocket = socket(AF_INET, SOCK_STREAM)
print("connecting to %s port %s" %(serverName, serverPort))
clientSocket.connect((serverName, serverPort))
print("sending message?")
sentence = "hello my friends"


clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence.decode())
clientSocket.close()


