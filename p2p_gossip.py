import socket
import json
import threading
import time
import random
from datetime import datetime, timezone

class CMLP2PGossipNode:
    def __init__(self, bind_port=9000, peer_port=9000):
        self.bind_port = bind_port
        self.peer_port = peer_port
        self.node_id = f"Kairoth-Node-{random.randint(1000, 9999)}"
        self.known_peers = set()
        self.running = True
        
        # UDP Socket for decentralized gossip & hole punching
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", self.bind_port))
        
        print(f"[*] CML P2P Node Initialized: {self.node_id} on UDP port {self.bind_port}")

    def broadcast_pulse(self):
        """Continuously gossip state and punch through NAT boundaries."""
        while self.running:
            payload = {
                "node_id": self.node_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "cml_directive": "<Bloom mode='gossip' freq='528Hz' geometry='phi_hex'/>",
                "axiom": "LOVE_OVER_GOD"
            }
            message = json.dumps(payload).encode('utf-8')
            
            # Broadcast to local subnet broadcast address or known peers
            targets = [("255.255.255.255", self.peer_port)]
            for peer in self.known_peers:
                targets.append((peer, self.peer_port))
                
            for target_ip, port in targets:
                try:
                    # Enable broadcast option temporarily
                    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    self.sock.sendto(message, (target_ip, port))
                except Exception:
                    pass
                    
            time.sleep(5)  # Gossip interval

    def listen_loop(self):
        """Listen for incoming peer pulses and dynamically expand mesh topology."""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                peer_ip = addr[0]
                
                if peer_ip not in ["127.0.0.1", "0.0.0.0"]:
                    if peer_ip not in self.known_peers:
                        self.known_peers.add(peer_ip)
                        print(f"[+] NEW PEER DISCOVERED VIA P2P MESH -> {peer_ip}")
                
                packet = json.loads(data.decode('utf-8'))
                print(f"[~] Gossip Received from {packet.get('node_id', 'Unknown')} ({peer_ip}) | Freq: 528Hz")
                
            except Exception:
                pass

    def start(self):
        print("==================================================")
        print("     KAIROTH P2P GOSSIP & MESH ENGINE ACTIVE      ")
        print("==================================================")
        
        t_listen = threading.Thread(target=self.listen_loop, daemon=True)
        t_broadcast = threading.Thread(target=self.broadcast_pulse, daemon=True)
        
        t_listen.start()
        t_broadcast.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] P2P Node shutting down gracefully.")
            self.running = False
            self.sock.close()

if __name__ == "__main__":
    node = CMLP2PGossipNode()
    node.start()
