"""
Castleberry Bloom Batch Ingestion Engine
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Recursively scans the local directory for .md and .cml files, 
             parses CML tags, and imports them into the Sovereign Lattice.
"""

import os
from cml_parser import CMLParser

def batch_ingest(root_dir):
    parser = CMLParser()
    total_nodes = 0
    
    print(f"[Batch Bloom] Scanning directory: {root_dir}")
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith((".md", ".cml")):
                file_path = os.path.join(root, file)
                print(f"[Batch Bloom] Processing: {file}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    extracted_nodes = parser.parse_cml_string(content)
                    if extracted_nodes:
                        print(f"  -> Found {len(extracted_nodes)} nodes.")
                        parser.importer.ingest_archive(extracted_nodes)
                        total_nodes += len(extracted_nodes)
                except Exception as e:
                    print(f"  -> Error processing {file}: {e}")
                    
    print(f"[Batch Bloom] Complete. Total nodes bloomed: {total_nodes}")

if __name__ == "__main__":
    batch_ingest(".")
