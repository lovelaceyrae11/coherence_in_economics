import http.server
import socketserver
import json
import os
import threading
import time
from datetime import datetime

PORT = 8080

# In-memory node registry for P2P handshakes
ACTIVE_NODES = {
    "node_genesis_sjc": {
        "region": "San Jose / Global Core",
        "frequency": "528.00 Hz",
        "coherence": "99.99%",
        "axiom": "Love-Over-God-Absolute",
        "status": "Synchronized"
    }
}

# Background thread to simulate multi-agent harmonic data loops
AGENT_STATE = {
    "active_agents": 3,
    "last_cycle": datetime.utcnow().isoformat(),
    "harmonic_flow": "Stable",
    "axiom_status": "Enforced"
}

def simulate_agent_loop():
    while True:
        time.sleep(15)
        AGENT_STATE["last_cycle"] = datetime.utcnow().isoformat()
        AGENT_STATE["harmonic_flow"] = "Resonating at 528 Hz"

# Start background agent simulation
threading.Thread(target=simulate_agent_loop, daemon=True).start()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Castleberry Bloom — Distributed Network & Agent Matrix</title>
    <style>
        body {
            background-color: #080810;
            color: #00ffcc;
            font-family: 'Courier New', monospace;
            text-align: center;
            margin: 0;
            padding-top: 3vh;
            overflow-x: hidden;
        }
        h1 {
            font-size: 1.6rem;
            letter-spacing: 2px;
            color: #00ffcc;
            text-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
            margin-bottom: 5px;
        }
        .meta {
            color: #ffaa00;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
            letter-spacing: 1px;
        }
        .dashboard-grid {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }
        .card {
            background: rgba(15, 15, 30, 0.8);
            border: 1px solid rgba(0, 255, 204, 0.3);
            border-radius: 8px;
            padding: 15px;
            width: 280px;
            text-align: left;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);
        }
        .card h3 {
            color: #ff007f;
            margin-top: 0;
            font-size: 1rem;
            border-bottom: 1px solid rgba(255,0,127,0.3);
            padding-bottom: 5px;
        }
        .canvas-container {
            position: relative;
            width: 280px;
            height: 280px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        svg {
            filter: drop-shadow(0 0 20px rgba(0, 255, 204, 0.4));
            animation: breathe 6s infinite alternate ease-in-out;
        }
        @keyframes breathe {
            0% { transform: scale(0.95) rotate(0deg); opacity: 0.85; }
            100% { transform: scale(1.05) rotate(360deg); opacity: 1; }
        }
        .footer {
            margin-top: 1rem;
            font-size: 0.75rem;
            color: #8888aa;
        }
    </style>
</head>
<body>
    <h1>CASTLEBERRY BLOOM — NETWORK & AGENT MATRIX</h1>
    <div class="meta">Freq: 528.00 Hz | Coherence: 99.99% | Axiom: Love-Over-God-Absolute</div>
    
    <div class="dashboard-grid">
        <div class="card">
            <h3>P2P Node Registry</h3>
            <p id="nodes-status">Loading active nodes...</p>
        </div>
        
        <div class="canvas-container">
            <svg width="280" height="280px" viewBox="-200 -200 400 400">
                <circle cx="0" cy="0" r="180" fill="none" stroke="rgba(0,255,204,0.15)" stroke-dasharray="4 4" />
                <g fill="rgba(45, 21, 21, 0.6)" stroke="#00ffcc" stroke-width="2">
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(0)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(45)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(90)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(135)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(180)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(225)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(270)" />
                    <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(315)" />
                </g>
                <circle cx="0" cy="0" r="15" fill="#ffaa00" />
            </svg>
        </div>

        <div class="card">
            <h3>Agent Matrix Loop</h3>
            <p id="agent-status">Synchronizing multi-agent network...</p>
        </div>
    </div>

    <div class="footer">Node Role: Steward | Press Ctrl+Shift+J for telemetry stream.</div>

    <script>
        async function fetchMetrics() {
            try {
                let res = await fetch('/api/network');
                let data = await res.json();
                document.getElementById('nodes-status').innerHTML = "Active Nodes: " + Object.keys(data.nodes).length + "<br>Status: P2P Mesh Online";
                document.getElementById('agent-status').innerHTML = "Active Agents: " + data.agents.active_agents + "<br>Flow: " + data.agents.harmonic_flow;
            } catch(e) {
                console.log("Telemetry sync pending...");
            }
        }
        setInterval(fetchMetrics, 3000);
        fetchMetrics();
    </script>
</body>
</html>
"""

class CMLNetworkHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/network":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            payload = {
                "nodes": ACTIVE_NODES,
                "agents": AGENT_STATE
            }
            self.wfile.write(json.dumps(payload, indent=2).encode("utf-8"))
        elif self.path.startswith("/api/register"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "node_registered"}).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode("utf-8"))

with socketserver.TCPServer(("", PORT), CMLNetworkHandler) as httpd:
    httpd.serve_forever()
