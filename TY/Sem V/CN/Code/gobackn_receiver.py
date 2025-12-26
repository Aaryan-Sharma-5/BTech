import socket
import json
from enum import Enum

class PacketType(Enum):
    DATA = "DATA"
    ACK = "ACK"

class GoBackNReceiver:
    def __init__(self, host='localhost', port=8081):
        self.host = host
        self.port = port
        self.expected_seq = 1
        self.socket = None
        self.total_packets = 0
        self.received_packets = 0
        
    def start_receiver(self):
        """Start the receiver server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            print(f"Go-Back-N Receiver listening on {self.host}:{self.port}")
            print("Waiting for sender connection...\n")
            
            conn, addr = self.socket.accept()
            print(f"Connected to sender at {addr}")
            print("=" * 60)
            print(f"{'PACKET':<10} {'EXPECTED':<10} {'STATUS':<15} {'ACTION'}")
            print("=" * 60)
            
            self.handle_packets(conn)
            
        except Exception as e:
            print(f"Receiver error: {e}")
        finally:
            if self.socket:
                self.socket.close()
    
    def handle_packets(self, conn):
        """Handle incoming packets from sender"""
        try:
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                
                try:
                    packet = json.loads(data)
                    if packet['type'] == PacketType.DATA.value:
                        self.process_data_packet(packet, conn)
                    elif packet['type'] == 'END':
                        print("\n" + "=" * 60)
                        print("Transmission complete!")
                        print(f"Total packets received correctly: {self.received_packets}")
                        break
                except json.JSONDecodeError:
                    continue
                    
        except Exception as e:
            print(f"Error handling packets: {e}")
        finally:
            conn.close()
    
    def process_data_packet(self, packet, conn):
        """Process received data packet and send ACK"""
        seq_num = packet['seq_num']
        
        if seq_num == self.expected_seq:
            # Packet received in order
            print(f"{seq_num:<10} {self.expected_seq:<10} {'ACCEPTED':<15} Send ACK {seq_num}")
            self.expected_seq += 1
            self.received_packets += 1
            self.send_ack(conn, seq_num)
        else:
            # Out of order packet - discard and send last correct ACK
            last_correct_ack = self.expected_seq - 1
            print(f"{seq_num:<10} {self.expected_seq:<10} {'DISCARDED':<15} Send ACK {last_correct_ack}")
            self.send_ack(conn, last_correct_ack)
    
    def send_ack(self, conn, ack_num):
        """Send acknowledgment packet"""
        ack_packet = {
            'type': PacketType.ACK.value,
            'ack_num': ack_num
        }
        try:
            conn.send(json.dumps(ack_packet).encode('utf-8'))
        except Exception as e:
            print(f"Error sending ACK: {e}")

if __name__ == "__main__":
    receiver = GoBackNReceiver()
    try:
        receiver.start_receiver()
    except KeyboardInterrupt:
        print("\nReceiver stopped by user")
    except Exception as e:
        print(f"Receiver error: {e}")
