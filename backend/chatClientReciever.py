import socket
import encryption
import server

client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1',port))

# Receive connection message from server
recv_msg = client_socket.recv(1024)
print(recv_msg.decode('utf-8'))

# Send user details to server
username = input("Enter your user name (prefix with #): ").strip().encode('utf-8')
client_socket.send(username)

while True:
    message = client_socket.recv(2048).decode('utf-8')

    if message.startswith("#"):
        # Server message
        recv_message = message[1:]
        
    elif message.startswith("@"):
        # Direct message from another user
        sender, content = message.split(':', 1)[1]
        private_key = encryption.read_private_key()
        decrypt_message = encryption.decrypt(content,private_key)
        recv_message = sender + decrypt_message.decode('utf-8')
        
        
    else:
        # Broadcast message from another user
        recv_message = message

    