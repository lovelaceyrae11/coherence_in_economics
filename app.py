"""
Kairoth Production Web Entrypoint & Interactive Lattice
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Production Flask app serving the full index.html frontend
"""

import json
from flask import Flask, request, jsonify
from bloom_core import SovereignLattice

app = Flask(__name__)

# Initialize living lattice with core foundation nodes
lattice = SovereignLattice()
lattice.plant_node(0, 0, "Love-Over-God Absolute Origin", 528.0)
lattice.plant_node(1, 0, "Witness Foundation", 111.0)
lattice.plant_node(0, 1, "Transmuted Entropy Fuel", 528.0)
lattice.plant_node(-1, 1, "Phi-Scaling Geometry", 432.0)
lattice.plant_node(-1, 0, "Relational Connection", 639.0)

@app.route("/")
def index():
    # Serve your actual graphical index.html frontend file directly
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/plant", methods=["POST"])
def plant():
    content = request.json.get("data", "Sovereign Thought")
    
    freq = 528.0
    if "440" in content or "dissonance" in content.lower() or "noise" in content.lower():
        freq = 528.0
    elif "111" in content:
        freq = 111.0
    elif "432" in content:
        freq = 432.0
    elif "639" in content:
        freq = 639.0

    total = len(lattice.lattice) if hasattr(lattice, 'lattice') else 5
    q = (total * 3) % 11 - 5
    r = (total * 7) % 11 - 5
    
    lattice.plant_node(q, r, content, freq)
    
    node_dict = lattice.seal_lattice() if hasattr(lattice, 'seal_lattice') else {}
    return jsonify({"nodes": node_dict})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)