# .venv\Scripts\activate.bat

# User Client side

# Standard procedure
# Run the server.py on server
# User run this file
# Register
# Enter the username with a ‘#’ prefix. Example: #alice
# Send the message to a user by following the format @username:message. Example: @bob:Hello, Bob! This is alice
# Repeat step 2 for other users. (Maximum 5 users is allowed with server configuration i.e. server_socket.listen(5)


import socket

client_socket = socket.socket()
port = 12345
client_socket.connect(("127.0.0.1", port))

# recieve connection message from server
recv_msg = client_socket.recv(1024)
print(recv_msg)

# send user details to server
send_msg = input("Enter your user name(prefix with #):")
client_socket.send(send_msg)


# receive and send message from/to different user/s

while True:
    recv_msg = client_socket.recv(1024)
    print(recv_msg)
    send_msg = input("Send your message in format [@user:message] ")
    if send_msg == "exit":
        break
    else:
        client_socket.send(send_msg)

client_socket.close()
