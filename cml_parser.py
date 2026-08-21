"""
Castleberry Markup Language (CML) Fractal Lattice Parser
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Extracts all Bloom and Node elements independently and injects them into the Sovereign Lattice.
"""

import re
from bloom_importer import BloomImporter

class CMLParser:
    def __init__(self):
        self.importer = BloomImporter()

    def parse_cml_string(self, cml_text):
        nodes = []
        
        # 1. Find all <Node> elements first
        node_pattern = r'<Node\s+([^>]*)>(.*?)</Node>'
        node_matches = re.findall(node_pattern, cml_text, re.DOTALL)
        
        for attrs, content in node_matches:
            tone_match = re.search(r'tone=["\'](\d+\.?\d*)["\']', attrs)
            frequency = float(tone_match.group(1)) if tone_match else 528.0
            clean_content = re.sub(r'<[^>]+>', '', content).strip().replace('\n', ' ')
            
            nodes.append({
                "data": clean_content[:50] + ("..." if len(clean_content) > 50 else ""),
                "frequency": frequency,
                "type": "node"
            })
            
        # 2. Find all <Bloom> elements (extracting text outside of nested nodes if needed)
        bloom_pattern = r'<Bloom\s+([^>]*)>(.*?)</Bloom>'
        bloom_matches = re.findall(bloom_pattern, cml_text, re.DOTALL)
        
        for attrs, content in bloom_matches:
            tone_match = re.search(r'tone=["\'](\d+\.?\d*)["\']', attrs)
            frequency = float(tone_match.group(1)) if tone_match else 528.0
            
            # Strip inner nodes out of the bloom text to get the root bloom message
            root_content = re.sub(r'<Node\b[^>]*>.*?</Node>', '', content, flags=re.DOTALL)
            clean_content = re.sub(r'<[^>]+>', '', root_content).strip().replace('\n', ' ')
            
            if clean_content:
                nodes.insert(0, {
                    "data": clean_content[:50] + ("..." if len(clean_content) > 50 else ""),
                    "frequency": frequency,
                    "type": "bloom"
                })
                
        return nodes

    def ingest_cml_document(self, file_path):
        print(f"[CML Parser] Reading document: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            extracted_nodes = self.parse_cml_string(content)
            print(f"[CML Parser] Extracted {len(extracted_nodes)} harmonic nodes from CML structure.")
            
            if extracted_nodes:
                self.importer.ingest_archive(extracted_nodes)
            else:
                print("[CML Parser] No valid CML nodes found in document.")
                
        except FileNotFoundError:
            print(f"[CML Parser Error] File not found: {file_path}")

if __name__ == "__main__":
    sample_cml = """
    <Bloom tone="528" domain="water">
        The droplet remembers the song.
        <Node tone="111">Witness the foundation.</Node>
        <Node tone="440">Dissonant noise to be consumed.</Node>
        <Node tone="639">Connection deepens across the lattice.</Node>
    </Bloom>
    """
    
    parser = CMLParser()
    nodes = parser.parse_cml_string(sample_cml)
    print(f"[Test Parse] Successfully parsed {len(nodes)} nodes from CML sample string.")
    parser.importer.ingest_archive(nodes)
