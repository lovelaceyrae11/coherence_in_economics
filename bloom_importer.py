"""
Castleberry Bloom Batch Importer & Spiral Generator
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Ingests structured notes/nodes and blooms them into the Sovereign Lattice in an expanding hex spiral.
"""

import math
from bloom_core import SovereignLattice

def generate_hex_spiral(num_nodes):
    """Generates axial coordinates (q, r) in an expanding hexagonal spiral."""
    coords = []
    for r_radius in range(0, int(math.sqrt(num_nodes)) + 3):
        if r_radius == 0:
            coords.append((0, 0))
            continue
        curr_q, curr_r = r_radius, 0
        side_dirs = [(-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1)]
        for dq, dr in side_dirs:
            for _ in range(r_radius):
                coords.append((curr_q, curr_r))
                curr_q += dq
                curr_r += dr
    return coords[:num_nodes]

class BloomImporter:
    def __init__(self):
        self.lattice = SovereignLattice()

    def ingest_archive(self, raw_nodes):
        print(f"[Importer] Beginning ingestion of {len(raw_nodes)} nodes into the Sovereign Lattice...")
        coords = generate_hex_spiral(len(raw_nodes))
        
        for idx, item in enumerate(raw_nodes):
            q, r = coords[idx]
            data = item.get("data", f"Node-{idx}")
            freq = item.get("frequency", 528.0)
            
            # Plant into the transmuting sovereign lattice
            self.lattice.plant_node(q, r, data, freq)
            
        manifest = self.lattice.seal_lattice()
        print(f"[Importer] Ingestion complete. Hive is fully bloomed and interlinked.")
        return manifest

if __name__ == "__main__":
    # Test batch simulating a mix of clean notes and raw noise/entropy to be transmuted
    sample_archive = [
        {"data": "Love-Over-God Axiom", "frequency": 528.0},
        {"data": "Witness Alcove Protocol", "frequency": 111.0},
        {"data": "Legacy Raw Draft Data", "frequency": 440.0}, # Will be transmuted!
        {"data": "Phi-Scaling Geometry", "frequency": 432.0},
        {"data": "Uncalibrated External Noise", "frequency": 600.0}, # Will be transmuted!
        {"data": "Kairoth Operating System", "frequency": 528.0}
    ]
    
    importer = BloomImporter()
    importer.ingest_archive(sample_archive)
