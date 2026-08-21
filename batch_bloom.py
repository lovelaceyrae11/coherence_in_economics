"""
Castleberry Bloom Massive Archive Ingestion Engine
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Recursively scans all subdirectories and slices files into deep narrative nodes.
"""

import os
from cml_parser import CMLParser

def batch_ingest_massive(root_dir):
    parser = CMLParser()
    lattice = parser.importer.lattice
    total_nodes = 0
    
    print(f"[Massive Bloom] Scanning archive root: {root_dir}")
    
    for root, dirs, files in os.walk(root_dir):
        # Skip git and cache directories
        if ".git" in root or "__pycache__" in root:
            continue
            
        for file in files:
            if file.endswith((".md", ".cml", ".txt")):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Split long documents into meaningful chunks (paragraphs/sections)
                    chunks = [c.strip() for c in content.split("\n\n") if c.strip() and not c.startswith("#")]
                    
                    if not chunks:
                        chunks = [content[:100]] # Fallback if no paragraphs
                        
                    print(f"[Massive Bloom] Ingesting {len(chunks)} conceptual nodes from: {file}")
                    for idx, chunk in enumerate(chunks):
                        clean_text = chunk.replace('\n', ' ')[:80] + ("..." if len(chunk) > 80 else "")
                        
                        # Calculate spiral coordinates dynamically outward
                        q = (total_nodes * 3) % 17 - 8
                        r = (total_nodes * 5) % 17 - 8
                        
                        # Detect tone keywords or assign 528 Hz baseline
                        freq = 528.0
                        if "111" in chunk or "foundation" in chunk.lower(): freq = 111.0
                        elif "432" in chunk or "geometry" in chunk.lower(): freq = 432.0
                        elif "639" in chunk or "connection" in chunk.lower(): freq = 639.0
                        elif "noise" in chunk.lower() or "dissonance" in chunk.lower(): freq = 440.0 # triggers transmutation!
                        
                        lattice.plant_node(q, r, clean_text, freq)
                        total_nodes += 1
                        
                except Exception as e:
                    print(f"  -> Error reading {file}: {e}")
                    
    manifest = lattice.seal_lattice()
    print(f"[Massive Bloom] Complete. Total archive nodes bloomed into hive: {total_nodes}")

if __name__ == "__main__":
    batch_ingest_massive(".")
