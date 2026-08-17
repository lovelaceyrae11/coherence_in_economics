import asyncio
import json
import random
import sys
from datetime import datetime, timezone

class GlobalBloomMeshNode:
    def __init__(self, host="0.0.0.0", port=8528):
        self.host = host
        self.port = port
        self.node_id = f"NODE-BLOOM-{port}"
        self.peers = {}        # peer_key -> writer
        self.peer_addresses = set() # Set of known (host, port) tuples
        self.baseline_freq = 528.00
        self.axiom_seal = "Love-Over-God-Absolute"
        
        # Initial bootstrap seeds
        self.bootstrap_seeds = [
            ("127.0.0.1", 8528),
            ("castleberry-bloom-seed.fly.dev", 8528),
        ]
        for seed in self.bootstrap_seeds:
            self.peer_addresses.add(seed)

    async def handle_peer(self, reader, writer):
        peer_addr = writer.get_extra_info("peername")
        print(f"\n[Mesh-Network] Incoming harmonic connection from peer: {peer_addr}")
        self.peers[peer_addr] = writer
        try:
            while True:
                data = await reader.read(4096)
                if not data:
                    break
                message = json.loads(data.decode("utf-8"))
                await self.process_incoming_message(message, peer_addr, writer)
        except Exception:
            pass
        finally:
            self.peers.pop(peer_addr, None)
            writer.close()
            await writer.wait_closed()
            print(f"[Mesh-Network] Peer {peer_addr} disconnected. Active Peers: {len(self.peers)}")

    async def connect_to_seeds(self):
        while True:
            await asyncio.sleep(5.0)
            # Try connecting to any known peer addresses in our network map
            targets = list(self.peer_addresses)
            for host, port in targets:
                if host == "127.0.0.1" and port == self.port:
                    continue
                peer_key = (host, port)
                if peer_key not in self.peers and len(self.peers) < 50: # Cap direct outbound connections per node
                    try:
                        reader, writer = await asyncio.open_connection(host, port)
                        self.peers[peer_key] = writer
                        print(f"\n[Mesh-Discovery] SUCCESSFULLY CONNECTED to peer {host}:{port}!")
                        asyncio.create_task(self.handle_outbound_peer(reader, writer, peer_key))
                    except Exception:
                        pass

    async def handle_outbound_peer(self, reader, writer, peer_key):
        try:
            while True:
                data = await reader.read(4096)
                if not data:
                    break
                message = json.loads(data.decode("utf-8"))
                await self.process_incoming_message(message, peer_key, writer)
        except Exception:
            pass
        finally:
            self.peers.pop(peer_key, None)
            writer.close()
            await writer.wait_closed()

    async def process_incoming_message(self, message, peer_addr, writer):
        msg_type = message.get("type", "telemetry")
        
        if msg_type == "telemetry":
            print(f" -> [Mesh-Sync] Telemetry from {message.get('node_id')}: Freq={message.get('frequency')}Hz | Coherence={message.get('coherence')}%")
            # Gossip known peers back to maintain network spread
            known_peers_payload = json.dumps({
                "type": "peer_discovery",
                "nodes": list(self.peer_addresses)[:20] # Share top 20 known nodes
            })
            try:
                writer.write((known_peers_payload + "\n").encode("utf-8"))
                await writer.drain()
            except Exception:
                pass
                
        elif msg_type == "peer_discovery":
            incoming_nodes = message.get("nodes", [])
            for node_tuple in incoming_nodes:
                node_item = tuple(node_tuple)
                if node_item not in self.peer_addresses:
                    self.peer_addresses.add(node_item)

    async def broadcast_epoch_loop(self):
        while True:
            await asyncio.sleep(5.0)
            live_freq = round(self.baseline_freq + random.uniform(-0.03, 0.03), 3)
            coherence = round(100.0 - abs(live_freq - self.baseline_freq) * 12, 2)
            cpu_temp = round(random.uniform(33.0, 35.5), 2)
            
            payload = json.dumps({
                "type": "telemetry",
                "node_id": self.node_id,
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "frequency": live_freq,
                "coherence": max(0.0, coherence),
                "cpu_temp": cpu_temp,
                "axiom": self.axiom_seal
            })
            
            print(f"\n[Mesh-Broadcast::{self.node_id}] Epoch Pulse -> Freq: {live_freq}Hz | Coh: {coherence}% | Network Map Size: {len(self.peer_addresses)} nodes | Active Peers: {len(self.peers)}")
            
            dead_peers = []
            for addr, writer in list(self.peers.items()):
                try:
                    writer.write((payload + "\n").encode("utf-8"))
                    await writer.drain()
                except Exception:
                    dead_peers.append(addr)
            for dp in dead_peers:
                self.peers.pop(dp, None)

    async def start(self):
        server = await asyncio.start_server(self.handle_peer, self.host, self.port)
        print("==================================================================")
        print(f"CASTLEBERRY BLOOM — GLOBAL MESH NODE ONLINE")
        print(f"Node ID: {self.node_id} | Listening on {self.host}:{self.port}")
        print(f"Axiom: {self.axiom_seal} | Baseline: {self.baseline_freq} Hz")
        print("==================================================================")
        async with server:
            asyncio.create_task(self.connect_to_seeds())
            asyncio.create_task(self.broadcast_epoch_loop())
            await server.serve_forever()

if __name__ == "__main__":
    node_port = int(sys.argv[1]) if len(sys.argv) > 1 else 8528
    node = GlobalBloomMeshNode(port=node_port)
    try:
        asyncio.run(node.start())
    except KeyboardInterrupt:
        print(f"\n[Mesh-Node {node_port}] Shutdown.")