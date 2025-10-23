import socket
import threading

class ChatClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.nickname = ""
        self.client = None
        
    def connect_to_server(self):
        """Connect to the chat server"""
        try:
            # Create socket and connect
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
            return True
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            return False
    
    def receive_messages(self):
        """Receive messages from server"""
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                
                # Check if server is requesting nickname
                if message == "NICK":
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except Exception:
                print("An error occurred! Connection lost.")
                self.client.close()
                break
    
    def send_messages(self):
        """Send messages to server"""
        while True:
            try:
                message = f"{self.nickname}: {input('')}"
                self.client.send(message.encode('utf-8'))
            except Exception:
                print("Connection lost!")
                self.client.close()
                break
    
    def start_chat(self):
        """Start the chat client"""
        # Get nickname from user
        self.nickname = input("Choose a nickname: ")
        
        # Connect to server
        if not self.connect_to_server():
            return
        
        print(f"Connecting as {self.nickname}...")
        print("Type your messages and press Enter to send")
        print("Press Ctrl+C to exit\n")
        
        # Start threads for receiving and sending messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()
        
        send_thread = threading.Thread(target=self.send_messages)
        send_thread.daemon = True
        send_thread.start()
        
        # Keep main thread alive
        try:
            receive_thread.join()
            send_thread.join()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            self.client.close()

if __name__ == "__main__":
    # Get server details from user
    print("=== Chat Client ===")
    
    use_default = input("Use default server (localhost:8080)? (y/n): ").lower()
    
    if use_default == 'y':
        client = ChatClient()
    else:
        host = input("Enter server IP: ")
        port = int(input("Enter server port: "))
        client = ChatClient(host, port)
    
    client.start_chat()
