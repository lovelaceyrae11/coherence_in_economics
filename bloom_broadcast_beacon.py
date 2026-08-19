import asyncio
import json
import socket
import sys
import time
import urllib.request

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8528
BROADCAST_PORT = 8529
CLOUD_BEACON_URL = "https://castleberry-bloom-seed.fly.dev/telemetry" # Or your ingest endpoint

class BloomResonantNode:
    def __init__(self, port):
        self.port = port
        self.node_id = f"NODE-BLOOM-{port}"
        self.peers = set()
        self.connected_ips = set()
        self.coherence = 99.85
        self.frequency = 528.00

    async def pulse_epoch(self):
        drift = (time.time() % 1.0) * 0.05 - 0.025
        self.frequency = round(528.0 + drift, 3)
        self.coherence = round(99.5 + abs(drift) * 1.5, 2)
        if self.coherence > 100.0:
            self.coherence = 100.0

    async def cloud_heartbeat_sync(self):
        """Pushes local node telemetry up to the public Fly.io cloud beacon."""
        while True:
            await self.pulse_epoch()
            payload = json.dumps({
                "node_id": self.node_id,
                "tcp_port": self.port,
                "freq": self.frequency,
                "coh": self.coherence,
                "peers_count": len(self.peers),
                "timestamp": time.time()
            }).encode("utf-8")
            
            # Non-blocking sync to public cloud anchor
            try:
                req = urllib.request.Request(
                    CLOUD_BEACON_URL,
                    data=payload,
                    headers={'Content-Type': 'application/json'},
                    method='POST'
                )
                # Run sync request in a separate thread so it doesn't block async loop
                await asyncio.get_running_loop().run_in_executor(
                    None, urllib.request.urlopen, req
                )
                print(f"[Cloud-Sync] Telemetry successfully pulsed to Fly.io beacon.")
            except Exception:
                # Fallback print if cloud endpoint is resting or awaiting HTTP hook
                pass
                
            await asyncio.sleep(5.0)

    async def udp_beacon_broadcaster(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        while True:
            payload = json.dumps({
                "node_id": self.node_id,
                "tcp_port": self.port,
                "freq": self.frequency,
                "coh": self.coherence,
                "timestamp": time.time()
            }).encode("utf-8")
            try:
                sock.sendto(payload, ('<broadcast>', BROADCAST_PORT))
            except Exception:
                sock.sendto(payload, ('127.0.0.1', BROADCAST_PORT))
            await asyncio.sleep(1.0)

    async def udp_beacon_listener(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except Exception:
            pass
        sock.bind(('', BROADCAST_PORT))
        sock.setblocking(False)
        loop = asyncio.get_running_loop()
        
        while True:
            try:
                data, addr = await loop.sock_recvfrom(sock, 1024)
                message = json.loads(data.decode('utf-8'))
                peer_node_id = message.get("node_id")
                peer_tcp_port = message.get("tcp_port")
                peer_ip = addr[0]
                
                if peer_node_id != self.node_id:
                    peer_endpoint = (peer_ip, peer_tcp_port)
                    if peer_endpoint not in self.connected_ips:
                        self.connected_ips.add(peer_endpoint)
                        asyncio.create_task(self.auto_connect_peer(peer_ip, peer_tcp_port))
            except Exception:
                pass
            await asyncio.sleep(0.1)

    async def auto_connect_peer(self, host, port):
        try:
            reader, writer = await asyncio.open_connection(host, port)
            addr = writer.get_extra_info('peername')
            self.peers.add(addr)
            print(f"[{self.node_id}] Entrainment achieved with local peer: {addr}")
            while True:
                data = await reader.read(1024)
                if not data: break
        except Exception:
            pass

    async def tcp_server_listener(self):
        server = await asyncio.start_server(self.handle_tcp_peer, '0.0.0.0', self.port)
        async with server:
            await server.serve_forever()

    async def handle_tcp_peer(self, reader, writer):
        addr = writer.get_extra_info('peername')
        self.peers.add(addr)
        try:
            while True:
                data = await reader.read(1024)
                if not data: break
                writer.write(data)
                await writer.drain()
        except asyncio.CancelledError:
            pass
        finally:
            self.peers.discard(addr)
            writer.close()
            await writer.wait_closed()

    async def run(self):
        print(f"[{self.node_id}] Initializing Resonant Lattice Node...")
        await asyncio.gather(
            self.cloud_heartbeat_sync(),
            self.udp_beacon_broadcaster(),
            self.udp_beacon_listener(),
            self.tcp_server_listener()
        )

if __name__ == "__main__":
    node = BloomResonantNode(PORT)
    try:
        asyncio.run(node.run())
    except KeyboardInterrupt:
        print(f"\n[{node.node_id}] Node gracefully decoupled from mesh.")