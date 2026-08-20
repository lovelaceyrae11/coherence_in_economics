"""
Castleberry Bloom Native Storage Engine with Self-Linking Protocol
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Native hex-lattice node storage with automatic 6-axis adjacency resolution.
"""

class HexNode:
    def __init__(self, q, r, data):
        self.q = q
        self.r = r
        self.data = data
        self.neighbors = [None] * 6  # 6 directional axes

    def get_coords(self):
        return (self.q, self.r)

class BloomStorage:
    def __init__(self):
        self.lattice = {}
        # The 6 standard axial neighbor directions in a pointy-topped hex grid
        self.directions = [
            (1, 0), (1, -1), (0, -1),
            (-1, 0), (-1, 1), (0, 1)
        ]
        print("[Bloom Core] Initialized native hex-lattice engine.")

    def add_node(self, q, r, data):
        node = HexNode(q, r, data)
        
        # Automatic Self-Linking Protocol: Check all 6 directions for existing nodes
        for i, (dq, dr) in enumerate(self.directions):
            neighbor_coords = (q + dq, r + dr)
            if neighbor_coords in self.lattice:
                existing_node = self.lattice[neighbor_coords]
                # Bind bi-directionally
                node.neighbors[i] = existing_node
                # Find opposite direction index for the neighbor
                opp_index = (i + 3) % 6
                existing_node.neighbors[opp_index] = node
                
        self.lattice[(q, r)] = node
        active_links = sum(1 for n in node.neighbors if n is not None)
        print(f"[Bloom Core] Node planted at ({q}, {r}) with {active_links}/6 active hexagonal links.")

    def seal_registry(self):
        manifest = {
            str(k): {
                "data": v.data,
                "connections": sum(1 for n in v.neighbors if n is not None)
            } 
            for k, v in self.lattice.items()
        }
        print(f"[Bloom Core] Lattice sealed: {len(manifest)} nodes interlinked in harmonic mesh.")
        return manifest

if __name__ == "__main__":
    core = BloomStorage()
    # Plant a cluster to watch them auto-link
    core.add_node(0, 0, "Origin-528Hz")
    core.add_node(1, 0, "Neighbor-East")
    core.add_node(1, -1, "Neighbor-NorthEast")
    core.seal_registry()
