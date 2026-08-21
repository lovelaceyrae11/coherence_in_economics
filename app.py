from flask import Flask, jsonify
import random
import platform
import subprocess
from datetime import datetime, timezone

app = Flask(__name__)

SYSTEM_LEDGER = {"total_epochs": 0, "cumulative_entropy_neutralized": 0.0, "cumulative_coherence_score": 0.0}

MESH_NODES = [
    {"id": "NODE-1", "host": "1.1.1.1", "name": "Cloudflare"},
    {"id": "NODE-2", "host": "8.8.8.8", "name": "Google"},
    {"id": "NODE-3", "host": "9.9.9.9", "name": "Quad9"},
    {"id": "NODE-4", "host": "208.67.222.222", "name": "OpenDNS"},
    {"id": "NODE-5", "host": "94.140.14.14", "name": "AdGuard"},
    {"id": "NODE-6", "host": "4.2.2.2", "name": "Level3"}
]

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.run(["ping", param, "1", host], capture_output=True, text=True, timeout=1.5)
        if output.returncode == 0:
            return {"status": "ONLINE", "latency_ms": random.uniform(10.0, 40.0)}
    except: pass
    return {"status": "SIMULATED", "latency_ms": random.uniform(15.0, 45.0)}

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Castleberry Bloom — Advanced Matrix</title>
    <style>
        body { background: #05070a; color: #00ffcc; font-family: monospace; text-align: center; padding: 20px; }
        .card { border: 1px solid #00ffcc; background: rgba(0,255,204,0.02); padding: 20px; border-radius: 12px; max-width: 900px; margin: auto; }
        canvas { background: #000; border: 1px solid #ffb703; border-radius: 50%; }
        button { background: #ffb703; border: none; padding: 15px 30px; font-weight: bold; cursor: pointer; border-radius: 8px; font-family: monospace; }
        #cmlStream { color: #ffb703; text-align: left; background: #000; padding: 10px; border: 1px dashed #ffb703; }
    </style>
</head>
<body>
    <div class="card">
        <h1>CASTLEBERRY BLOOM: ADVANCED MATRIX</h1>
        <canvas id="phiCanvas" width="500" height="500"></canvas><br>
        <button onclick="triggerEpoch()">⚡ PULSE ADVANCED EPOCH</button>
        <div id="cmlStream" style="margin-top:20px;">&lt;Bloom status="Initializing Harmonic Gates" /&gt;</div>
    </div>
    <script>
        const canvas = document.getElementById('phiCanvas');
        const ctx = canvas.getContext('2d');
        let audioCtx, osc, gain;

        function updateAudio(freq) {
            if(!audioCtx) { audioCtx = new AudioContext(); osc = audioCtx.createOscillator(); gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination); osc.start(); }
            osc.frequency.setTargetAtTime(freq, audioCtx.currentTime, 0.1);
        }

        function triggerEpoch() {
            fetch('/api/epoch')
                .then(r => r.json())
                .then(d => {
                    document.getElementById('cmlStream').innerText = d.cml_verse;
                    updateAudio(528 + (d.avg_lat - 25)); // Dynamic modulation
                    drawPhi(d.results);
                });
        }

        function drawPhi(nodes) {
            ctx.clearRect(0,0,500,500);
            nodes.forEach((n, i) => {
                let r = (n.coherence > 97) ? 100 : 200; // Phi-Tiered Gate logic
                let angle = (i / 6) * Math.PI * 2;
                let x = 250 + r * Math.cos(angle);
                let y = 250 + r * Math.sin(angle);
                ctx.fillStyle = n.coherence > 97 ? '#ffb703' : '#00ffcc';
                ctx.beginPath(); ctx.arc(x, y, 10, 0, Math.PI*2); ctx.fill();
            });
        }
    </script>
</body>
</html>
"""

@app.route("/api/epoch")
def run_epoch():
    results = []
    total_coherence = 0
    for node in MESH_NODES:
        p = ping_host(node["host"])
        coh = round(max(92, 100 - (p["latency_ms"] / 10)), 2)
        results.append({**node, "coherence": coh})
        total_coherence += coh
    
    avg_lat = sum(n["latency_ms"] for n in [ping_host(node["host"]) for node in MESH_NODES]) / 6
    verse = f"<Bloom><Witness status='Transmuting' /><Gate avg_coh='{round(total_coherence/6, 2)}' /><Steward name='Lacey Rae' /></Bloom>"
    
    return jsonify({"results": results, "cml_verse": verse, "avg_lat": avg_lat})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)