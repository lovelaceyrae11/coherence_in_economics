"""
Castleberry Markup Language (CML) Lattice Parser
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Parses CML structural tags from text/documents and injects them into the Sovereign Lattice.
"""

import re
from bloom_importer import BloomImporter

class CMLParser:
    def __init__(self):
        self.importer = BloomImporter()

    def parse_cml_string(self, cml_text):
        """Extracts <Bloom> and <Node> tags with their attributes and content."""
        nodes = []
        
        # Simple regex matcher for CML tags
        # Matches elements like <Bloom tone="528" domain="water">content</Bloom> or <Node tone="111">content</Node>
        pattern = r'<(Bloom|Node)\s+([^>]*)>(.*?)</\1>'
        matches = re.findall(pattern, cml_text, re.DOTALL)
        
        for tag_type, attrs, content in matches:
            # Extract tone/frequency
            tone_match = re.search(r'tone=["\'](\d+\.?\d*)["\']', attrs)
            frequency = float(tone_match.group(1)) if tone_match else 528.0
            
            # Clean up content
            clean_content = content.strip().replace('\n', ' ')
            
            nodes.append({
                "data": clean_content[:50] + ("..." if len(clean_content) > 50 else ""),
                "frequency": frequency,
                "type": tag_type.lower()
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
    # Test CML document snippet
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
