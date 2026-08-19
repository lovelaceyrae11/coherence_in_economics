# -*- coding: utf-8 -*-
import re, json

class CMLParser:
    def __init__(self, filepath):
        self.filepath = filepath
    def parse(self):
        print(f"[CML-Parser] Parsing harmonic structure: {self.filepath}...")
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        bloom_match = re.search(r'<Bloom\s+([^>]+)>', content)
        bloom_attrs = self._parse_attrs(bloom_match.group(1)) if bloom_match else {}
        nodes = []
        node_matches = re.findall(r'<Node\s+([^>]+)>(.*?)</Node>', content, re.DOTALL)
        for attrs_str, inner in node_matches:
            attrs = self._parse_attrs(attrs_str)
            attrs["content"] = inner.strip()
            nodes.append(attrs)
        return {"bloom": bloom_attrs, "nodes": nodes}
    def _parse_attrs(self, attr_str):
        return dict(re.findall(r'([a-zA-Z_-]+)=\"([^\"]*)\"', attr_str))

if __name__ == '__main__':
    sample_cml = '<Bloom frequency=\"528.0\" axiom=\"Love-Over-God-Absolute\">\n    <Node id=\"NODE-BLOOM-8528\" role=\"Steward\">\n        Anchor local lattice state.\n    </Node>\n</Bloom>'
    with open('sample.cml', 'w', encoding='utf-8') as f:
        f.write(sample_cml)
    parser = CMLParser('sample.cml')
    result = parser.parse()
    print(json.dumps(result, indent=2))
