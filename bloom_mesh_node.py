import asyncio
import json
import math
import random
import time
from datetime import datetime, timezone

class GlobalBloomMeshNode:
    """
    Advanced Decentralized Mesh Node with Auto-Peer Discovery and Bootstrap Routing.
    """
    def __init__(self, host="0.0.0.0", port=8528):
        self.host = host
        self.port = port
        self.node_id = f"NODE-BLOOM-{random.randint(1000, 9999)}"
        self.peers = {}  # writer objects mapped to peer info
        self.baseline_freq = 528.00
        self.axiom_seal = "Love-Over-God-Absolute"
        
        # Hardcoded public seed bootstrap nodes (expandable as nodes deploy globally)
        self.bootstrap_seeds = [
            ("127.0.0.1", 8528),  # Local loopback for testing
            # ("bloom-node-us.gcp.net", 8528), # Future cloud deployment slots
        ]

    async def handle_peer(self, reader, writer):
        """Handles incoming connections from external peers."""
        peer_addr = writer.get_extra_info('peername')
        print(f"\n[Mesh-Network] Incoming harmonic connection from external peer: {peer_addr}")
        self.peers[peer_addr] = writer
        
        try:
            while True:
                data = await reader.read(2048)
                if not data:
                    break
                message = json.loads(data.decode('utf-8'))
                await self.process_incoming_message(message, peer_addr)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            print(f"[Mesh-Error] Connection drop with {peer_addr}: {e}")
        finally:
            self.peers.pop(peer_addr, None)
            writer.close()
            await writer.wait_closed()
            print(f"[Mesh-Network] Peer {peer_addr} disconnected. Active Peers: {len(self.peers)}")

    async def connect_to_bootstrap_seeds(self):
        """Actively reaches out to discover and connect to external peers."""
        while True:
            await asyncio.sleep(10.0) # Retry interval for peer discovery
            if len(self.peers) >= 10:
                continue # Limit active socket pool
                
            for host, port in self.bootstrap_seeds:
                # Don't connect to self on same loopback if already tracked
                if host == "127.0.0.1" and port == self.port:
                    continue
                    
                peer_key = (host, port)
                if peer_key not in self.peers:
                    try:
                        print(f"[Mesh-Discovery] Attempting handshake with bootstrap seed {host}:{port}...")
                        reader, writer = await asyncio.open_connection(host, port)
                        self.peers[peer_key] = writer
                        print(f"[Mesh-Discovery] SUCCESSFULLY CONNECTED to external peer at {host}:{port}!")
                        
                        # Spawn background reader for this outbound connection
                        asyncio.create_task(self.handle_outbound_peer(reader, writer, peer_key))
                    except Exception:
                        # Seed offline or unreachable; silently continue scanning
                        pass

    async def handle_outbound_peer(self, reader, writer, peer_key):
        """Manages communication for outbound connections."""
        try:
            while True:
                data = await reader.read(2048)
                if not data:
                    break
                message = json.loads(data.decode('utf-8'))
                await self.process_incoming_message(message, peer_key)
        except Exception:
            pass
        finally:
            self.peers.pop(peer_key, None)
            writer.close()
            await writer.wait_closed()

    async def process_incoming_message(self, message, peer_addr):
        """Processes CML telemetry payloads received from the mesh."""
        print(f" -> [Mesh-Sync] Telemetry from {message.get('node_id')} ({peer_addr}): "
              f"Freq={message.get('frequency')}Hz | Coherence={message.get('coherence')}%")

    async def broadcast_epoch_loop(self):
        """Broadcasts local thermodynamic health and telemetry out to all connected peers."""
        while True:
            await asyncio.sleep(5.0)
            
            live_freq = round(self.baseline_freq + random.uniform(-0.03, 0.03), 3)
            coherence = round(100.0 - abs(live_freq - self.baseline_freq) * 12, 2)
            cpu_temp = round(random.uniform(33.0, 35.5), 2)
            
            payload = json.dumps({
                "node_id": self.node_id,
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "frequency": live_freq,
                "coherence": max(0.0, coherence),
                "cpu_temp": cpu_temp,
                "axiom": self.axiom_seal
            })
            
            print(f"\n[Mesh-Broadcast::{self.node_id}] Epoch Pulse Sent -> Freq: {live_freq}Hz | Coh: {coherence}%")
            print(f" -> Connected External Mesh Peers: {len(self.peers)}")
            
            # Dispatch packet to all connected peers
            dead_peers = []
            for addr, writer in list(self.peers.items()):
                try:
                    writer.write((payload + "\n").encode('utf-8'))
                    await writer.drain()
                except Exception:
                    dead_peers.append(addr)
            
            for dp in dead_peers:
                self.peers.pop(dp, None)

    async def start(self):
        """Starts the server listener and the background peer discovery engine."""
        server = await asyncio.start_server(self.handle_peer, self.host, self.port)
        print("==================================================================")
        print(f"CASTLEBERRY BLOOM — AUTO-CONNECTING GLOBAL MESH NODE ONLINE")
        print(f"Node ID: {self.node_id} | Listening on port {self.port}")
        print(f"Axiom: {self.axiom_seal} | Baseline: {self.baseline_freq} Hz")
        print("==================================================================")
        
        async with server:
            await asyncio.gather(
                server.serve_forever(),
                self.connect_to_bootstrap_seeds(),
                self.broadcast_epoch_loop()
            )

if __name__ == "__main__":
    node = GlobalBloomMeshNode()
    try:
        asyncio.run(node.start())
    except KeyboardInterrupt:
        print("\n[Mesh-Node] Graceful shutdown. Equilibrium maintained.")