import socket
import threading
import time
import json
from enum import Enum

class PacketType(Enum):
    DATA = "DATA"
    ACK = "ACK"

class FixedGoBackNSender:
    def __init__(self, host='localhost', port=8081, total_packets=9, window_size=3, loss_rate=5):
        self.host = host
        self.port = port
        self.total_packets = total_packets
        self.window_size = window_size
        self.loss_rate = loss_rate
        
        # Protocol state variables
        self.base = 1
        self.next_seq_num = 1
        self.sender_attempts = 0
        self.received_acks = 0
        
        # Socket and synchronization
        self.socket = None
        self.running = True
        self.lock = threading.Lock()
        
        # Timeout settings
        self.timeout = 2.0
        self.last_activity_time = time.time()
        
    def connect_to_receiver(self):
        """Connect to the receiver"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Connected to Go-Back-N Receiver at {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"Failed to connect to receiver: {e}")
            return False
    
    def start_sender(self):
        """Start the Go-Back-N sender"""
        if not self.connect_to_receiver():
            return
        
        print("\nGo-Back-N Protocol Simulation")
        print("=" * 70)
        print(f"Total Packets: {self.total_packets}, Window Size: {self.window_size}, Loss Pattern: Every {self.loss_rate}th packet")
        print("=" * 70)
        print(f"{'ATTEMPT':<10} {'SEND_PKT':<10} {'STATUS':<15} {'ACTION'}")
        print("=" * 70)
        
        # Start ACK receiver thread
        ack_thread = threading.Thread(target=self.receive_acks)
        ack_thread.daemon = True
        ack_thread.start()
        
        # Main sending loop - continue until all packets are acknowledged
        while self.base <= self.total_packets and self.running:
            # Send packets within window
            while (self.next_seq_num < self.base + self.window_size and 
                   self.next_seq_num <= self.total_packets):
                self.send_packet(self.next_seq_num)
                self.next_seq_num += 1
                self.last_activity_time = time.time()
            
            # Wait for ACKs with timeout
            time.sleep(0.1)  # Small delay for ACK processing
            
            # Check for timeout
            current_time = time.time()
            if current_time - self.last_activity_time > self.timeout:
                if self.base <= self.total_packets:
                    print(f"{'TIMEOUT':<10} {'--':<10} {'TIMEOUT':<15} Retransmit from {self.base}")
                    self.next_seq_num = self.base  # Go back to base
                    self.last_activity_time = current_time
        
        # Send end signal
        if self.running:
            end_packet = {'type': 'END'}
            try:
                self.socket.send(json.dumps(end_packet).encode('utf-8'))
            except Exception:
                pass
        
        # Print final statistics
        print("\n" + "=" * 70)
        print(f"Final attempts (sender transmissions): {self.sender_attempts}")
        print(f"Final ACKs received: {self.received_acks}")
        print("Transmission completed successfully!")
        
        self.cleanup()
    
    def send_packet(self, seq_num):
        """Send a data packet"""
        self.sender_attempts += 1
        
        # Simulate packet loss based on pattern
        packet_lost = (self.sender_attempts % self.loss_rate == 0)
        
        packet = {
            'type': PacketType.DATA.value,
            'seq_num': seq_num,
            'data': f"Data packet {seq_num}"
        }
        
        if packet_lost:
            # Simulate packet loss - don't actually send
            print(f"{self.sender_attempts:<10} {seq_num:<10} {'LOST':<15} Packet dropped")
        else:
            try:
                self.socket.send(json.dumps(packet).encode('utf-8'))
                print(f"{self.sender_attempts:<10} {seq_num:<10} {'SENT':<15} Packet transmitted")
            except Exception as e:
                print(f"Error sending packet {seq_num}: {e}")
                self.running = False
    
    def receive_acks(self):
        """Receive ACK packets from receiver"""
        try:
            while self.running:
                self.socket.settimeout(0.1)  # Short timeout for non-blocking behavior
                try:
                    data = self.socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    
                    packet = json.loads(data)
                    if packet['type'] == PacketType.ACK.value:
                        ack_num = packet['ack_num']
                        self.process_ack(ack_num)
                except socket.timeout:
                    continue
                except json.JSONDecodeError:
                    continue
                    
        except Exception as e:
            if self.running:
                print(f"Error receiving ACKs: {e}")
    
    def process_ack(self, ack_num):
        """Process received ACK"""
        with self.lock:
            if ack_num >= self.base:
                print(f"{'ACK':<10} {ack_num:<10} {'RECEIVED':<15} ACK for packet {ack_num}")
                self.base = ack_num + 1
                self.received_acks += 1
                self.last_activity_time = time.time()  # Reset timeout on successful ACK
            else:
                print(f"{'ACK':<10} {ack_num:<10} {'DUPLICATE':<15} Duplicate ACK ignored")
    
    def cleanup(self):
        """Clean up resources"""
        self.running = False
        if self.socket:
            self.socket.close()

def main():
    print("Go-Back-N Sender (Fixed Version)")
    print("================================")
    
    # Get configuration from user or use defaults
    use_defaults = input("Use default settings? (y/n): ").lower().strip()
    
    if use_defaults == 'y':
        sender = FixedGoBackNSender()
    else:
        try:
            host = input("Enter receiver host (localhost): ").strip() or 'localhost'
            port = int(input("Enter receiver port (8081): ").strip() or 8081)
            packets = int(input("Enter total packets (9): ").strip() or 9)
            window = int(input("Enter window size (3): ").strip() or 3)
            loss_rate = int(input("Enter loss pattern - every Kth packet (5): ").strip() or 5)
            
            sender = FixedGoBackNSender(host, port, packets, window, loss_rate)
        except ValueError:
            print("Invalid input. Using default settings.")
            sender = FixedGoBackNSender()
    
    try:
        sender.start_sender()
    except KeyboardInterrupt:
        print("\nSender stopped by user")
        sender.cleanup()
    except Exception as e:
        print(f"Sender error: {e}")
        sender.cleanup()

if __name__ == "__main__":
    main()
