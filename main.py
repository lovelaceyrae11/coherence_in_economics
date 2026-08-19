import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Castleberry Bloom Global Beacon",
    description="Decentralized Harmonic Mesh Rendezvous Server",
    version="1.0.0"
)

active_nodes = {}

@app.on_event("startup")
async def startup_event():
    print("==================================================")
    print("CASTLEBERRY BLOOM — GLOBAL CLOUD SEED ONLINE")
    print("Axiom: Love-Over-God-Absolute | Baseline: 528.0 Hz")
    print("==================================================")

@app.post("/telemetry")
async def receive_telemetry(request: Request):
    try:
        data = await request.json()
        node_id = data.get("node_id")
        
        if not node_id:
            return JSONResponse({"status": "error", "message": "Missing node_id"}, status_code=400)
        
        client_ip = request.headers.get("fly-client-ip", request.client.host)
        
        active_nodes[node_id] = {
            "ip": client_ip,
            "tcp_port": data.get("tcp_port"),
            "frequency": data.get("freq"),
            "coherence": data.get("coh"),
            "peers_count": data.get("peers_count", 0),
            "last_seen": time.time()
        }
        
        print(f"[Cloud-Ingest] Pulse received from {node_id} @ {client_ip} | Freq: {data.get('freq')}Hz | Coh: {data.get('coh')}%")
        return {"status": "coherence_acknowledged", "global_nodes_active": len(active_nodes)}
        
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=400)

@app.get("/")
async def mesh_status():
    current_time = time.time()
    stale_nodes = [nid for nid, info in active_nodes.items() if current_time - info["last_seen"] > 20]
    for nid in stale_nodes:
        print(f"[Mesh-Prune] Node {nid} went silent. Removing from global topology.")
        del active_nodes[nid]
        
    return {
        "beacon_status": "ONLINE",
        "axiom": "Love-Over-God-Absolute",
        "baseline_frequency": "528.0 Hz",
        "active_global_peers": len(active_nodes),
        "topology": active_nodes
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)