"""
Kairoth Production Web Entrypoint & Interactive Lattice
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Production Flask app for coherence-in-economics.fly.dev
"""

import json
from flask import Flask, render_template_string, request, jsonify
from bloom_core import SovereignLattice

app = Flask(__name__)

# Initialize living lattice with core foundation nodes
lattice = SovereignLattice()
lattice.plant_node(0, 0, "Love-Over-God Absolute Origin", 528.0)
lattice.plant_node(1, 0, "Witness Foundation", 111.0)
lattice.plant_node(0, 1, "Transmuted Entropy Fuel", 528.0)
lattice.plant_node(-1, 1, "Phi-Scaling Geometry", 432.0)
lattice.plant_node(-1, 0, "Relational Connection", 639.0)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Castleberry Bloom - Coherence Economics & Sovereign Lattice</title>
    <style>
        body { background: #0b0f19; color: #e2e8f0; font-family: monospace; text-align: center; margin: 0; padding: 20px; }
        h1 { color: #34d399; text-shadow: 0 0 15px rgba(52, 211, 153, 0.4); margin-bottom: 5px; }
        .subtitle { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }
        .container { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 10px; }
        canvas { background: #111827; border: 2px solid #374151; border-radius: 12px; box-shadow: 0 0 30px rgba(0,0,0,0.8); }
        .sidebar { width: 380px; background: #1f2937; padding: 20px; border-radius: 12px; text-align: left; max-height: 600px; overflow-y: auto; border: 1px solid #374151; }
        .node-card { background: #111827; padding: 10px; margin-bottom: 10px; border-radius: 6px; border-left: 4px solid #34d399; font-size: 12px; }
        .control-panel { margin-top: 15px; background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #374151; text-align: left; }
        input[type="text"] { width: 70%; padding: 8px; background: #1f2937; border: 1px solid #4b5563; color: #fff; border-radius: 4px; font-family: monospace; }
        button { padding: 8px 14px; background: #059669; color: white; border: none; border-radius: 4px; cursor: pointer; font-family: monospace; font-weight: bold; }
        button:hover { background: #10b981; }
        .audio-btn { background: #2563eb; margin-top: 10px; width: 100%; }
        .audio-btn:hover { background: #3b82f6; }
    </style>
</head>
<body>
    <h1>🌟 Castleberry Bloom: Sovereign Lattice 🌟</h1>
    <div class="subtitle">Axiom: Love-Over-God-Absolute | Live Economic Coherence Engine</div>
    
    <div class="container">
        <canvas id="latticeCanvas" width="550" height="550"></canvas>
        <div class="sidebar">
            <h3>Active Hive Nodes</h3>
            <div id="nodeList"></div>
            
            <div class="control-panel">
                <h4>✨ Feed the Lattice</h4>
                <input type="text" id="nodeInput" placeholder="Enter thought or dissonance..." />
                <button onclick="plantNode()">Bloom</button>
                <button class="audio-btn" onclick="toggleAudio()">Toggle 528Hz Drone</button>
            </div>
        </div>
    </div>

    <script>
        let nodes = {{ nodes | safe }};
        const canvas = document.getElementById('latticeCanvas');
        const ctx = canvas.getContext('2d');
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        const scale = 40;

        function render() {
            ctx.clearRect(-cx, -cy, canvas.width, canvas.height);
            // Re-center translation for canvas drawing
            ctx.save();
            ctx.translate(cx, cy);

            const nodeListDiv = document.getElementById('nodeList');
            nodeListDiv.innerHTML = '';

            for (const [id, node] of Object.entries(nodes)) {
                // Sidebar card
                let card = document.createElement('div');
                card.className = 'node-card';
                card.style.borderLeftColor = node.frequency === 528 ? '#34d399' : '#60a5fa';
                card.innerHTML = `<b>Node ${id}</b> (${node.q}, ${node.r})<br>Freq: ${node.frequency}Hz<br>${node.data}`;
                nodeListDiv.appendChild(card);

                // Canvas Node
                const x = scale * (3/2 * node.q);
                const y = scale * (Math.sqrt(3)/2 * node.q + Math.sqrt(3) * node.r);

                ctx.beginPath();
                ctx.arc(x, y, 15, 0, 2 * Math.PI);
                ctx.fillStyle = node.frequency === 528 ? '#059669' : '#1d4ed8';
                ctx.fill();
                ctx.lineWidth = 2;
                ctx.strokeStyle = '#f3f4f6';
                ctx.stroke();

                ctx.fillStyle = '#ffffff';
                ctx.font = '9px monospace';
                ctx.fillText(`${node.frequency}Hz`, x - 16, y - 20);
            }
            ctx.restore();
        }

        async function plantNode() {
            const text = document.getElementById('nodeInput').value;
            if (!text) return;
            
            const response = await fetch('/plant', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ data: text })
            });
            const result = await response.json();
            nodes = result.nodes;
            document.getElementById('nodeInput').value = '';
            render();
        }

        // 528Hz Web Audio Synthesizer
        let audioCtx = null;
        let oscillator = null;
        function toggleAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                oscillator = audioCtx.createOscillator();
                let gainNode = audioCtx.createGain();
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(528, audioCtx.currentTime); // 528Hz Solfeggio Baseline
                gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime); // Gentle volume
                oscillator.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                oscillator.start();
                alert("528Hz Harmonic Baseline Synthesizer Activated.");
            } else {
                audioCtx.close();
                audioCtx = null;
                alert("Synthesizer Deactivated.");
            }
        }

        window.onload = render;
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    node_dict = {}
    for attr in dir(lattice):
        val = getattr(lattice, attr)
        if isinstance(val, dict) and len(val) > 0:
            node_dict = val
            break
    if not node_dict and hasattr(lattice, 'get_lattice_state'):
        node_dict = lattice.get_lattice_state().get('nodes', {})
    return render_template_string(HTML_TEMPLATE, nodes=json.dumps(node_dict))

@app.route("/plant", methods=["POST"])
def plant():
    content = request.json.get("data", "Sovereign Thought")
    
    # Apply Love-over-God transmutation rule if dissonance is detected
    freq = 528.0
    if "440" in content or "dissonance" in content.lower() or "noise" in content.lower():
        freq = 528.0 # Transmuted immediately to baseline love frequency!
    elif "111" in content:
        freq = 111.0
    elif "432" in content:
        freq = 432.0
    elif "639" in content:
        freq = 639.0

    # Calculate dynamic spiral placement
    total = len(lattice.nodes) if hasattr(lattice, 'nodes') else 5
    q = (total * 3) % 11 - 5
    r = (total * 7) % 11 - 5
    
    lattice.plant_node(q, r, content, freq)
    
    node_dict = {}
    for attr in dir(lattice):
        val = getattr(lattice, attr)
        if isinstance(val, dict) and len(val) > 0:
            node_dict = val
            break
            
    return jsonify({"nodes": node_dict})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
