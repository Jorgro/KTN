# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

from socket import *
import argparse as ap
import getpass as gp
import time
import ssl
import base64

#Get sender_email and recipient_email as arguments to the program
parser = ap.ArgumentParser(description='A test SMTP client without authentication')
parser.add_argument('-f', '--from', dest='fromMail', required=True, metavar='<sender_email>')
parser.add_argument('-t', '--to', dest='toMail', required=True, metavar='<recipient_email>')
#If using the authentication of the SMTP server, also get a valid username (optional exercise)
#parser.add_argument('-u', '--username', dest='username', required=True, metavar='<username>')

args = parser.parse_args()
fromMail = args.fromMail #Sender's email address
toMail = args.toMail #Recipient's email address
#username = args.username #SMTP username in case you are implementing the optional exercise

#If using the authentication of the SMTP server, ask for a valid password (optional exercise)
#password = gp.getpass(prompt='Password: ')

# Message to send
message_text = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no but it allows only authenticated communications. (optional exercise)
#mailserver = 'smtp.stud.ntnu.no'
# You can run a local simple SMTP server such as "Fake SMTP Server" and communicate with it without authentication.
mailserver = 'smtp.office365.com'

# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

heloCommand = 'EHLO Hey\r\n'
clientSocket.send(heloCommand.encode()) #Python 3
#clientSocket.send(heloCommand) #Python 2.7
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')

#TLS/SSL

command = "STARTTLS\r\n"
clientSocket.send(command.encode())
recv = clientSocket.recv(1024)
print(recv.decode())
clientSocketSSL = ssl.wrap_socket(clientSocket)


# Send HELO command and print server response.
# Can use EHLO instead since HELO is obsolete, but the latter can still be used
heloCommand = 'EHLO Hey\r\n'
clientSocketSSL.send(heloCommand.encode()) #Python 3
#clientSocket.send(heloCommand) #Python 2.7
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server.')

#authenticate
authCommand = 'AUTH LOGIN\r\n'
clientSocketSSL.send(authCommand.encode()) #Python 3
#clientSocket.send(heloCommand) #Python 2.7
recv = clientSocketSSL.recv(1024).decode()
print(recv)

authCommand = 'jorgro@stud.ntnu.no\r\n'
clientSocketSSL.send(base64.b64encode(authCommand.encode())) #Python 3
#clientSocket.send(heloCommand) #Python 2.7
#recv = clientSocketSSL.recv(1024).decode()
#print(recv)

authCommand = 'hoplite1\r\n'
clientSocketSSL.send(base64.b64encode(authCommand.encode())) #Python 3
#clientSocket.send(heloCommand) #Python 2.7
#recv = clientSocketSSL.recv(1024).decode()
#print(recv)



# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand= 'MAIL FROM:'+ fromMail +'\r\n'
clientSocketSSL.send(mailFromCommand.encode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptCommand= 'RCPT TO:' + toMail +'\r\n'
clientSocketSSL.send(rcptCommand.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand= 'DATA\r\n'
clientSocketSSL.send(dataCommand.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
# Fill in end

# Send message data.
# Fill in start
subj = "im a hacker"
date = time.strftime("%d/%m/%Y")
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"%(fromMail, toMail, subj, date, message_text)
clientSocketSSL.send(msg.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocketSSL.send(endmsg.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT'\r\n'"
clientSocketSSL.send(quitCommand.encode())

recv = clientSocketSSL.recv(1024).decode()
print(recv)
# Fill in end

#Note that there are more communications if you implement the optional exercise.
