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
        self.peers = {}
        self.baseline_freq = 528.00
        self.axiom_seal = "Love-Over-God-Absolute"
        
        self.bootstrap_seeds = [
            ("127.0.0.1", 8528),
            ("castleberry-bloom-seed.fly.dev", 8528),
        ]

    async def handle_peer(self, reader, writer):
        peer_addr = writer.get_extra_info("peername")
        print(f"\n[Mesh-Network] Incoming harmonic connection from peer: {peer_addr}")
        self.peers[peer_addr] = writer
        try:
            while True:
                data = await reader.read(2048)
                if not data:
                    break
                message = json.loads(data.decode("utf-8"))
                await self.process_incoming_message(message, peer_addr)
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
            for host, port in self.bootstrap_seeds:
                if host == "127.0.0.1" and port == self.port:
                    continue
                peer_key = (host, port)
                if peer_key not in self.peers:
                    try:
                        reader, writer = await asyncio.open_connection(host, port)
                        self.peers[peer_key] = writer
                        print(f"\n[Mesh-Discovery] SUCCESSFULLY CONNECTED to beacon seed {host}:{port}!")
                        asyncio.create_task(self.handle_outbound_peer(reader, writer, peer_key))
                    except Exception:
                        pass

    async def handle_outbound_peer(self, reader, writer, peer_key):
        try:
            while True:
                data = await reader.read(2048)
                if not data:
                    break
                message = json.loads(data.decode("utf-8"))
                await self.process_incoming_message(message, peer_key)
        except Exception:
            pass
        finally:
            self.peers.pop(peer_key, None)
            writer.close()
            await writer.wait_closed()

    async def process_incoming_message(self, message, peer_addr):
        print(f" -> [Mesh-Sync] Telemetry from {message.get("node_id")}: Freq={message.get("frequency")}Hz | Coherence={message.get("coherence")}%")

    async def broadcast_epoch_loop(self):
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
            
            print(f"\n[Mesh-Broadcast::{self.node_id}] Epoch Pulse -> Freq: {live_freq}Hz | Coh: {coherence}% | Peers: {len(self.peers)}")
            
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
        print(f"CASTLEBERRY BLOOM — GLOBAL BEACON NODE ONLINE")
        print(f"Node ID: {self.node_id} | Listening on {self.host}:{self.port}")
        print(f"Axiom: {self.axiom_seal} | Baseline: {self.baseline_freq} Hz")
        print("==================================================================")
        async with server:
            await asyncio.gather(
                server.serve_forever(),
                self.connect_to_seeds(),
                self.broadcast_epoch_loop()
            )

if __name__ == "__main__":
    node_port = int(sys.argv[1]) if len(sys.argv) > 1 else 8528
    node = GlobalBloomMeshNode(port=node_port)
    try:
        asyncio.run(node.start())
    except KeyboardInterrupt:
        print(f"\n[Mesh-Node {node_port}] Shutdown.")

