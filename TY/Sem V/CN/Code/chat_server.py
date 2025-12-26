import socket
import threading

class ChatServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.clients = []
        self.nicknames = []
        
    def start_server(self):
        # Create socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        
        print(f"Server is listening on {self.host}:{self.port}")
        print("Waiting for connections...")
        
        while True:
            # Accept new connections
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")
            
            # Request and receive nickname
            client.send("NICK".encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            
            # Store client info
            self.nicknames.append(nickname)
            self.clients.append(client)
            
            print(f"Nickname of client is {nickname}")
            self.broadcast(f"{nickname} joined the chat!".encode('utf-8'))
            client.send("Connected to server!".encode('utf-8'))
            
            # Create thread to handle the client
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()
    
    def broadcast(self, message):
        """Send message to all connected clients"""
        for client in self.clients:
            try:
                client.send(message)
            except Exception:
                # Remove client if sending fails
                self.remove_client(client)
    
    def handle_client(self, client):
        """Handle messages from a client"""
        while True:
            try:
                # Receive message from client
                message = client.recv(1024)
                if message:
                    self.broadcast(message)
                else:
                    self.remove_client(client)
                    break
            except Exception:
                self.remove_client(client)
                break
    
    def remove_client(self, client):
        """Remove a client from the server"""
        if client in self.clients:
            index = self.clients.index(client)
            self.clients.remove(client)
            nickname = self.nicknames[index]
            self.nicknames.remove(nickname)
            self.broadcast(f"{nickname} left the chat!".encode('utf-8'))
            client.close()

if __name__ == "__main__":
    try:
        server = ChatServer()
        server.start_server()
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    except Exception as e:
        print(f"Error: {e}")
