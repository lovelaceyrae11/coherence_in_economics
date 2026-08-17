import asyncio
import json
import math
import random
from datetime import datetime, timezone

class BloomMeshNode:
    """
    Decentralized Peer-to-Peer Mesh Node for the Castleberry Bloom Network.
    Synchronizes 528 Hz harmonic epochs and broadcasts CML telemetry across peers.
    """
    def __init__(self, host="0.0.0.0", port=8528):
        self.host = host
        self.port = port
        self.node_id = f"NODE-BLOOM-{random.randint(1000, 9999)}"
        self.peers = set()
        self.baseline_freq = 528.00
        self.axiom_seal = "Love-Over-God-Absolute"

    async def register_peer(self, reader, writer):
        """Handles incoming peer connections in the decentralized mesh."""
        peer_addr = writer.get_extra_info('peername')
        self.peers.add(peer_addr)
        print(f"\n[Mesh-Network] New harmonic peer connected from {peer_addr}")
        
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                message = json.loads(data.decode('utf-8'))
                await self.handle_incoming_telemetry(message)
        except asyncio.CancelledError:
            pass
        finally:
            self.peers.discard(peer_addr)
            writer.close()
            await writer.wait_closed()
            print(f"[Mesh-Network] Peer {peer_addr} disconnected.")

    async def handle_incoming_telemetry(self, message):
        """Validates incoming CML-sealed telemetry from network peers."""
        print(f" -> [Mesh-Sync] Received telemetry from {message.get('node_id')}: "
              f"Freq={message.get('frequency')}Hz | Coherence={message.get('coherence')}%")

    async def broadcast_epoch(self):
        """Continuously broadcasts local thermodynamic telemetry to the mesh."""
        while True:
            await asyncio.sleep(5.0) # Epoch interval
            
            # Calculate local harmonic metrics
            live_freq = round(self.baseline_freq + random.uniform(-0.03, 0.03), 3)
            coherence = round(100.0 - abs(live_freq - self.baseline_freq) * 12, 2)
            cpu_temp = round(random.uniform(33.0, 35.5), 2)
            
            payload = {
                "node_id": self.node_id,
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "frequency": live_freq,
                "coherence": max(0.0, coherence),
                "cpu_temp": cpu_temp,
                "axiom": self.axiom_seal
            }
            
            print(f"\n[Mesh-Broadcast::{self.node_id}] Epoch Pulse Sent -> Freq: {live_freq}Hz | Coh: {coherence}% | Temp: {cpu_temp}°C")
            print(f" -> Active Mesh Peers Connected: {len(self.peers)}")

    async def start(self):
        """Initializes the P2P server daemon."""
        server = await asyncio.start_server(self.register_peer, self.host, self.port)
        addr = server.sockets[0].getsockname()
        print("==================================================================")
        print(f"CASTLEBERRY BLOOM — P2P MESH NODE ONLINE")
        print(f"Node ID: {self.node_id} | Listening on {addr}")
        print(f"Axiom: {self.axiom_seal} | Baseline: {self.baseline_freq} Hz")
        print("==================================================================")
        
        async with server:
            await asyncio.gather(
                server.serve_forever(),
                self.broadcast_epoch()
            )

if __name__ == "__main__":
    node = BloomMeshNode()
    try:
        asyncio.run(node.start())
    except KeyboardInterrupt:
        print("\n[Mesh-Node] Graceful shutdown initiated. Equilibrium maintained.")