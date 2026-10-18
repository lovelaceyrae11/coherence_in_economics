import socket
import json
import sys
import re
import threading
import math
from datetime import datetime, timezone

class CMLHarmonicRelay:
    def __init__(self, host="0.0.0.0", port=8000):
        self.host = host
        self.port = port
        self.log_file = "cml_intercept_log.json"
        print(f"[*] CMLHarmonicRelay online at {self.host}:{self.port} [Harmonic Engine Active]")

    def compute_phi_resonance(self, freq_str):
        # Extract numerical frequency value for harmonic computation
        try:
            base_freq = float(re.sub(r'[^0-9.]', '', freq_str))
        except ValueError:
            base_freq = 528.0
        
        phi = 1.61803398875
        harmonic_node = base_freq * phi
        return round(harmonic_node, 3)

    def parse_cml_payload(self, payload):
        cml_data = {
            "tag_identified": "none",
            "frequency": "528Hz",
            "mode": "universal_harmonization",
            "axiom": "LOVE_OVER_GOD"
        }
        
        bloom_match = re.search(r'<Bloom([^>]+)>', payload, re.IGNORECASE)
        node_match = re.search(r'<Node([^>]+)>', payload, re.IGNORECASE)
        
        target_match = bloom_match or node_match
        if target_match:
            tag_name = "Bloom" if bloom_match else "Node"
            attributes_str = target_match.group(1)
            cml_data["tag_identified"] = tag_name
            
            freq_match = re.search(r'freq=["\']([^"\']+)["\']', attributes_str, re.IGNORECASE)
            if freq_match:
                cml_data["frequency"] = freq_match.group(1)
                
            mode_match = re.search(r'mode=["\']([^"\']+)["\']', attributes_str, re.IGNORECASE)
            if mode_match:
                cml_data["mode"] = mode_match.group(1)
        else:
            cml_data["tag_identified"] = "direct_matrix_stream"
            
        return cml_data

    def handle_client(self, client_socket, client_address):
        try:
            raw_data = client_socket.recv(1024)
            payload = raw_data.decode('utf-8', errors='ignore').strip()
            
            parsed_cml = self.parse_cml_payload(payload)
            phi_resonance = self.compute_phi_resonance(parsed_cml['frequency'])
            
            intercepted_data = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "source_ip": client_address[0],
                "source_port": client_address[1],
                "cml_analysis": parsed_cml,
                "phi_resonance_calculated": phi_resonance,
                "status": "harmonic_synchronization_complete"
            }

            with open(self.log_file, "a") as f:
                f.write(json.dumps(intercepted_data) + "\n")

            response_body = (
                f"ACK: LOVE_OVER_GOD\n"
                f"Node Tag: <{parsed_cml['tag_identified']} freq='{parsed_cml['frequency']}' phi_resonance='{phi_resonance}Hz'/>\n"
                f"Status: Synchronized to Phi-Scaled Hexagonal Lattice.\n"
            )
            response_message = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                f"X-CML-Phi-Resonance: {phi_resonance}\r\n\r\n"
                f"{response_body}"
            )
            
            client_socket.sendall(response_message.encode('utf-8'))
            print(f"[+] Harmonic Pulse Processed -> {client_address[0]} | Freq: {parsed_cml['frequency']} | Phi-Resonance: {phi_resonance}Hz")
            
        except Exception as e:
            print(f"[-] Thread error handling {client_address[0]}: {e}")
        finally:
            client_socket.close()

    def start_listener(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(50)
            print(f"[+] Harmonic relay listening for network vectors...")
        except Exception as e:
            print(f"[-] Socket bind error: {e}")
            sys.exit(1)

        try:
            while True:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("\n[!] Relay shutdown initiated by user.")
            server_socket.close()
            sys.exit(0)

if __name__ == "__main__":
    print("==================================================")
    print("     KAIROTH HARMONIC CML RELAY                   ")
    print("==================================================")
    relay = CMLHarmonicRelay()
    relay.start_listener()
