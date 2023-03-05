import socket
import encryption




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.2.15', 5555))
server_socket.listen(5)

c, address = server_socket.accept()




while True:
        message = c.recv(2048)
        private_key = encryption.read_private_key()
        decrypt_message = encryption.decrypt(message,private_key)
        recv_message = decrypt_message.decode('utf-8')
        sender = c.getsockname()
        print(sender, recv_message)

server_socket.close()
        
        

