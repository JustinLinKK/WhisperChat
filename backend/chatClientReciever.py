import socket
import encryption
import server


client_socket = socket.socket()
port = 12345
client_socket.bind(('localhost', port))
client_socket.listen(5)

c, addr = client_socket.accept()



while True:
    message = c.recv(2048).decode('utf-8')
    # Direct message from another user
    if not message:
            break
    private_key = encryption.read_private_key()
    decrypt_message = encryption.decrypt(message,private_key)
    recv_message = decrypt_message.decode('utf-8')
    sender = c.getsockname()
    server.forwardMessage(sender,'localhost' , recv_message)
        
        

    