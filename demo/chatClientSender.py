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


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket()



#Input message_body, userneame.
#Body message -> encode -> encryption -> sending
def send_message(send_msg:str,recipient):
    message = send_msg.encode('utf-8')
    public_key = encryption.read_public_key(recipient)
    encrypt_message = encryption.encrypt(message,public_key)
    send_msg:bytes = encrypt_message
    server_socket.send(send_msg)


while True:
    target = input("Input the target ip address:")
    server_socket.connect((target, 5555))
    while True:
        message = input("Input message:")
        send_message(message,target)
        if message == "exit0":
            server_socket.close()
            break



