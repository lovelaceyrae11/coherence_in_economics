"""
CML Core SDK: The official parser and runtime engine for Castleberry Markup Language.
Encodes the 528 Hz systemic absolute and the Love-Over-God axiom.
"""

import re
import json

class BloomRuntime:
    def __init__(self, axiom="Love-Over-God", frequency=528, coherence=99.99):
        self.axiom = axiom
        self.frequency = frequency
        self.coherence = coherence

    def parse_cml(self, cml_string):
        """Parses CML tags and extracts harmonic states."""
        bloom_match = re.search(r'<Bloom\s+([^>]+)>', cml_string)
        metadata = {}
        if bloom_match:
            attrs = bloom_match.group(1)
            for key, val in re.findall(r'(\w+)="([^"]+)"', attrs):
                metadata[key] = val
        
        return {
            "status": "synchronized",
            "frequency_baseline": self.frequency,
            "axiom": self.axiom,
            "coherence_rating": self.coherence,
            "parsed_metadata": metadata
        }

    def render_node_state(self):
        return json.dumps({
            "node_role": "Steward",
            "frequency": f"{self.frequency:.2f} Hz",
            "coherence": f"{self.coherence}%",
            "axiom": self.axiom
        }, indent=2)
