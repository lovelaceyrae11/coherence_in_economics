"""
Kairoth Production Web Entrypoint & Sovereign Lattice Host
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Production Flask entrypoint serving the ultimate Live Lattice Portal
"""

import os
from flask import Flask, send_from_directory, request, jsonify
from bloom_core import SovereignLattice

app = Flask(__name__, static_url_path='', static_folder='.')

# Initialize living lattice with core foundation nodes
lattice = SovereignLattice()
lattice.plant_node(0, 0, "Love-Over-God Absolute Origin", 528.0)
lattice.plant_node(1, 0, "Witness Foundation", 111.0)
lattice.plant_node(0, 1, "Transmuted Entropy Fuel", 528.0)
lattice.plant_node(-1, 1, "Phi-Scaling Geometry", 432.0)
lattice.plant_node(-1, 0, "Relational Connection", 639.0)

@app.route("/")
def serve_index():
    # Serve the ultimate full-screen index.html portal directly
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def serve_static_or_asset(path):
    # Serve any supporting CML files, scripts, or assets requested by the portal
    if os.path.exists(path):
        return send_from_directory(".", path)
    return "Resource not found", 404

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