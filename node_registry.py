"""
Node Registry Service: Tracks distributed CML nodes across the network,
aggregating coherence metrics and regional node statuses.
"""

import json
import os
from datetime import datetime

REGISTRY_FILE = "node_registry.json"

def register_node(node_id, region, frequency="528.00 Hz", coherence="99.99%"):
    nodes = load_registry()
    nodes[node_id] = {
        "region": region,
        "frequency": frequency,
        "coherence": coherence,
        "last_seen": datetime.utcnow().isoformat()
    }
    save_registry(nodes)
    return nodes

def load_registry():
    if os.path.exists(REGISTRY_FILE):
        try:
            with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_registry(nodes):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(nodes, f, indent=2)

if __name__ == "__main__":
    print("[Registry] Initializing central node registry schema...")
    save_registry({})
    print("[Registry] Ready for distributed network handshakes.")
