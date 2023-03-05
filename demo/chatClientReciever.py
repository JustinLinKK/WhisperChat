import socket
import encryption
import threading




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5555))
server_socket.listen(5)





def receive_messages():
    while True:
        c, address = server_socket.accept()
        message = c.recv(2048).decode('utf-8')
        if not message:
            break
        # Direct message from another user
        if message.startswith("#"):
            if encryption.read_public_key("localhost") == 3:
                private_key,public_key = encryption.generate_key_pairs
                public_key_str= encryption.public_key_to_string(public_key)
                encryption.store_private_key_file(private_key)
                encryption.store_public_key_file(public_key,"localhost")
            else:
                public_key = encryption.read_public_key("localhost")
                public_key_str= encryption.public_key_to_string(public_key)
            send_msg = "@" + public_key_str
            encryption.store_private_key_file(private_key)
            server_socket.send(send_msg.encode('utf-8'))

        elif message.startswith("@"):
            public_key_str = message[1:]
            public_key = encryption.public_string_to_key(public_key_str)
            encryption.store_public_key_file(public_key,c.getsockname)

        else:
            private_key = encryption.read_private_key()
            decrypt_message = encryption.decrypt(message,private_key)
            recv_message = decrypt_message.decode('utf-8')
            sender = c.getsockname()
            print(sender, recv_message)

    server_socket.close()
        
        

threading.Thread(target=receive_messages).start()

def send_message(send_msg,recipient):
    message = message.encode('utf-8')
    if encryption.read_public_key(recipient) == 3:
        server_socket.send("#".encode('utf-8'))
        send_message(send_msg,recipient)
    else:
        public_key = encryption.read_public_key(recipient)
        encrypt_message = encryption.encrypt(message,public_key)
        send_msg = encrypt_message
        server_socket.send(send_msg.encode('utf-8'))
    


while True:
    target = input("Input the target ip address:")
    server_socket.connect((target, 5555))
    while True:
        message = input("Input message:")
        send_message(message,target)
        if message == "exit0":
            server_socket.close()
            break

