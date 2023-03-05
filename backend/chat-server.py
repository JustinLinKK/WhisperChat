#Message-server

import socket
import select

PORT = 12345
SOCKET_LIST = []
USERS = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', PORT))
server_socket.listen(5)

SOCKET_LIST.append(server_socket)
print("Chat server started on port " + str(PORT))

def broadcast_data(sender_socket, message):
    """Send a message to all connected clients except the sender."""
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != sender_socket:
            try:
                socket.send(message.encode())
            except:
                # Remove the socket if it is no longer reachable
                socket.close()
                SOCKET_LIST.remove(socket)
                username = get_username(socket)
                if username:
                    print("Client " + username + " disconnected")

def get_username(client_socket):
    """Return the username associated with the client socket."""
    for username, socket in USERS.items():
        if socket == client_socket:
            return username
    return None

while True:
    # Use select to wait for incoming data or new connections
    read_sockets, _, _ = select.select(SOCKET_LIST, [], [], 0)

    for sock in read_sockets:
        if sock == server_socket:
            # Handle new connection requests
            client_socket, address = server_socket.accept()
            SOCKET_LIST.append(client_socket)
            print("Client connected from " + address[0] + ":" + str(address[1]))
            client_socket.send(("#You are connected from: " + address[0]).encode('utf-8'))
        else:
            # Handle incoming data from clients
            try:
                data = sock.recv(2048)
                if data:
                    data = data.decode('utf-8').strip()
                    if data.startswith("#"):
                        # Save the client's username
                        username = data[1:].lower()
                        USERS[username] = sock
                        print("User " + username + " added.")
                        message_send="#Your user detail saved as: " + username
                        sock.send(message_send.encode('utf-8'))
                        message_send="#" + username + "connected"
                        broadcast_data(sock, message_send.encode('utf-8'))
                    elif data.startswith("@"):
                        # Send a message to another client
                        recipient, message = data[1:].split(':', 1)
                        recipient_socket = USERS.get(recipient.lower())
                        if recipient_socket:
                            message_send = "@" + get_username(sock) + ": " + message
                            recipient_socket.send(message_send.encode('utf-8'))
                        else:
                            message_send="#User " + recipient + " not found"
                            sock.send(message_send.encode('utf-8'))
                    else:
                        # Broadcast the message to all clients
                        message_send = "@" + get_username(sock) + data
                        broadcast_data(sock, message_send.encode('utf-8'))
            except:
                # Remove the socket if it is no longer reachable
                socket.close()
                SOCKET_LIST.remove(socket)
                username = get_username(socket)
                if username:
                    print("Client " + username + " disconnected")
                    message_send = "#" + "Client " + username + " disconnected"
                    broadcast_data(None, message_send.encode('utf-8'))

