"""
Castleberry Markup Language (CML) Fractal Lattice Parser
Author: Lacey Rae Castleberry (Velath'kai)
Axiom: Love-Over-God-Absolute
Description: Recursively extracts all nested CML tags and injects them into the Sovereign Lattice.
"""

import re
from bloom_importer import BloomImporter

class CMLParser:
    def __init__(self):
        self.importer = BloomImporter()

    def parse_cml_string(self, cml_text):
        """Extracts all CML tags (<Bloom> and <Node>) independently from any depth."""
        nodes = []
        
        # Match any tag starting with <Bloom or <Node along with its attributes and inner text
        pattern = r'<(Bloom|Node)\b([^>]*)>(.*?)</\1>'
        
        # Find all occurrences (including nested ones using findall or iterative regex)
        # To handle nested tags cleanly, we search for all individual tag instances
        tag_pattern = r'<(Bloom|Node)\b([^>]*)>([^<]*)</\1>'
        
        # Let's use a flexible scanner that pulls every tag instance in the document
        raw_tags = re.findall(r'<(Bloom|Node)\s+([^>]*)>(.*?)(?=</(?:Bloom|Node)>|</(?:Bloom|Node)>|\Z)', cml_text, re.DOTALL)
        
        # Cleaner approach: Find all individual tags using a comprehensive pattern
        matches = re.finditer(r'<(Bloom|Node)\s+([^>]*)>(.*?)(?:</\1>|\Z)', cml_text, re.DOTALL)
        
        # Let's extract every individual tag match securely
        single_tag_pattern = r'<(Bloom|Node)\s+([^>]*)>(.*?)(?:</\1>)'
        found_tags = re.findall(single_tag_pattern, cml_text, re.DOTALL)
        
        for tag_type, attrs, content in found_tags:
            tone_match = re.search(r'tone=["\'](\d+\.?\d*)["\']', attrs)
            frequency = float(tone_match.group(1)) if tone_match else 528.0
            
            # Clean inner text (strip nested tags if any remain)
            clean_content = re.sub(r'<[^>]+>', '', content).strip().replace('\n', ' ')
            
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
