#User Client side

#Standard procedure
#Run the server.py on server
#User run this file
#Register  
#Enter the username with a ‘#’ prefix. Example: #alice
#Send the message to a user by following the format @username:message. Example: @bob:Hello, Bob! This is alice
#Repeat step 2 for other users. (Maximum 5 users is allowed with server configuration i.e. server_socket.listen(5)
#Run reciever before use this script function



import socket
import encryption



client_socket = socket.socket()
port = 12345


#Input message_body, userneame.
#Body message -> encode -> encryption -> sending
def send_message(send_msg,recipient):
    client_socket.connect((recipient,port))
    message = message.encode('utf-8')
    public_key = encryption.read_public_key(recipient)
    encrypt_message = encryption.encrypt(message,public_key)
    send_msg = encrypt_message
    client_socket.send(send_msg.encode('utf-8'))
    client_socket.close()





