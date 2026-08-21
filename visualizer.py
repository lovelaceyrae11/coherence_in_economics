"""
Kairoth Interactive Lattice Visualizer
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Serves a local web dashboard rendering the living Sovereign Lattice in real-time.
"""

import json
from flask import Flask, render_template_string
from bloom_core import SovereignLattice

app = Flask(__name__)

# Initialize and seed our living lattice for the dashboard
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
    <title>Castleberry Bloom - Sovereign Lattice Visualizer</title>
    <style>
        body { background: #0b0f19; color: #e2e8f0; font-family: monospace; text-align: center; margin: 0; padding: 20px; }
        h1 { color: #34d399; text-shadow: 0 0 15px rgba(52, 211, 153, 0.4); }
        .container { display: flex; justify-content: center; gap: 20px; margin-top: 20px; }
        canvas { background: #111827; border: 2px solid #374151; border-radius: 12px; box-shadow: 0 0 30px rgba(0,0,0,0.8); }
        .sidebar { width: 350px; background: #1f2937; padding: 20px; border-radius: 12px; text-align: left; max-height: 600px; overflow-y: auto; border: 1px solid #374151; }
        .node-card { background: #111827; padding: 10px; margin-bottom: 10px; border-radius: 6px; border-left: 4px solid #34d399; font-size: 12px; }
    </style>
</head>
<body>
    <h1>🌟 Castleberry Bloom: Sovereign Lattice 🌟</h1>
    <p>Axiom: Love-Over-God-Absolute | Baseline: 528 Hz</p>
    
    <div class="container">
        <canvas id="latticeCanvas" width="600" height="600"></canvas>
        <div class="sidebar">
            <h3>Active Hive Nodes</h3>
            <div id="nodeList"></div>
        </div>
    </div>

    <script>
        const nodes = {{ nodes | safe }};
        const canvas = document.getElementById('latticeCanvas');
        const ctx = canvas.getContext('2d');
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        const scale = 45;

        // Render Sidebar
        const nodeListDiv = document.getElementById('nodeList');
        for (const [id, node] of Object.entries(nodes)) {
            let card = document.createElement('div');
            card.className = 'node-card';
            card.style.borderLeftColor = node.frequency === 528 ? '#34d399' : '#60a5fa';
            card.innerHTML = `<b>Node ${id}</b> (${node.q}, ${node.r})<br>Freq: ${node.frequency}Hz<br>${node.data}`;
            nodeListDiv.appendChild(card);
        }

        // Draw Hex Grid & Nodes
        ctx.translate(cx, cy);
        
        for (const [id, node] of Object.entries(nodes)) {
            // Axial to pixel coordinate conversion
            const x = scale * (3/2 * node.q);
            const y = scale * (Math.sqrt(3)/2 * node.q + Math.sqrt(3) * node.r);

            // Draw node circle
            ctx.beginPath();
            ctx.arc(x, y, 16, 0, 2 * Math.PI);
            ctx.fillStyle = node.frequency === 528 ? '#059669' : '#1d4ed8';
            ctx.fill();
            ctx.lineWidth = 2;
            ctx.strokeStyle = '#f3f4f6';
            ctx.stroke();

            // Label
            ctx.fillStyle = '#ffffff';
            ctx.font = '10px monospace';
            ctx.fillText(`${node.frequency}Hz`, x - 18, y - 22);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    node_data = json.dumps(lattice.nodes)
    return render_template_string(HTML_TEMPLATE, nodes=node_data)

if __name__ == "__main__":
    print("[Visualizer] Starting Kairoth Web Dashboard at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
