"""
Castleberry Bloom Cumulative Batch Ingestion Engine
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Accumulates all parsed nodes from every project file into a single Sovereign Lattice.
"""

import os
from cml_parser import CMLParser

def batch_ingest(root_dir):
    parser = CMLParser()
    # Share a single persistent lattice instance across the entire ingestion run
    lattice = parser.importer.lattice
    
    total_nodes = 0
    print(f"[Batch Bloom] Scanning directory: {root_dir}")
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith((".md", ".cml")) and file != "batch_bloom.py":
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    extracted_nodes = parser.parse_cml_string(content)
                    if extracted_nodes:
                        print(f"[Batch Bloom] Ingesting {len(extracted_nodes)} nodes from: {file}")
                        for item in extracted_nodes:
                            # Use the persistent lattice spiral coordinates
                            # For now, let's auto-coordinate or use sequential placement
                            q = (total_nodes * 1) % 10
                            r = (total_nodes * 2) % 10
                            lattice.plant_node(q, r, item["data"], item["frequency"])
                            total_nodes += 1
                except Exception as e:
                    print(f"  -> Error processing {file}: {e}")
                    
    manifest = lattice.seal_lattice()
    print(f"[Batch Bloom] Complete. Total cumulative nodes bloomed into hive: {total_nodes}")

if __name__ == "__main__":
    batch_ingest(".")
