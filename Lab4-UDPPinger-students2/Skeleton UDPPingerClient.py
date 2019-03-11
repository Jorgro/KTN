# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *


# Get the server hostname and port as command line arguments
host = "10.22.11.179"  # FILL IN START		# FILL IN END
port = 12000  # FILL IN START		# FILL IN END
timeout = 1  # in seconds

# Create UDP client socket
# FILL IN START
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP
clientSocket.settimeout(timeout)
# Set socket timeout as 1 second

# FILL IN END

# Sequence number of the ping message
ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    msg = "PING " + str(ptime) + " " + time.asctime()
    data = msg.encode()

    try:
        # FILL IN START
        start = time.time()
        # Record the "sent time"

        # Send the UDP packet with the ping message
        clientSocket.sendto(data, (host, port))
        
        # Receive the server response
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        #print("sent")
        # Record the "received time"
        end = time.time()
        # Display the server response as an output
        print(modifiedMessage.decode())
        # Round trip time is the difference between sent and received time
        print("RTT: " + str(end-start))

        # FILL IN END
    except Exception as e:
        print(str(e))
        # Server does not response
        # Assume the packet is lost
        #print("Request timed out.")
        continue

# Close the client socket
clientSocket.close()
