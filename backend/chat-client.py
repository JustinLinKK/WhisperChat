#User Client side

#Standard procedure
#Run the server.py on server
#User run this file
#Register  
#Enter the username with a ‘#’ prefix. Example: #alice
#Send the message to a user by following the format @username:message. Example: @bob:Hello, Bob! This is alice
#Repeat step 2 for other users. (Maximum 5 users is allowed with server configuration i.e. server_socket.listen(5)

import socket
import encryption

client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1',port))

# Receive connection message from server
recv_msg = client_socket.recv(1024)
print(recv_msg.decode('utf-8'))

# Send user details to server
username = input("Enter your user name (prefix with #): ").strip().encode('utf-8')
client_socket.send(username)

# Receive  message from different users
def recv_message():
    recv_msg = client_socket.recv(1024)
    msg_body = recv_msg.split(b":", 1)[1]
    private_key = encryption.read_private_key()
    msg_decrypt = encryption.decrypt(msg_body)
    print(recv_msg.decode('utf-8'))


#Input message_body, userneame.
#Body message -> encode -> encryption -> sending
def send_message(send_msg,recipient):
    recipient = recipient.strip()
    message = message.encode('utf-8')
    public_key = encryption.read_public_key(recipient)
    encrypt_message = encryption.encrypt(message,public_key)
    send_msg = "@"+recipient+":"+encrypt_message
    client_socket.send(send_msg.encode('utf-8'))


