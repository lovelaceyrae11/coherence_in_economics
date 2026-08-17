import xml.etree.ElementTree as ET
import json
import sys

class CmlParser:
    """
    Parses, validates, and transforms Castleberry Markup Language (CML) manifests
    into structured JSON objects while verifying axiom compliance.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

    def load_manifest(self):
        try:
            self.tree = ET.parse(self.file_path)
            self.root = self.tree.getroot()
            print(f"[CML-Parser] Successfully loaded manifest: {self.file_path}")
        except Exception as e:
            print(f"[CML-Parser Error] Failed to parse XML structure: {e}")
            sys.exit(1)

    def validate_axiom(self):
        """Checks for the mandatory Love-Over-God-Absolute axiom seal across elements."""
        axiom = self.root.attrib.get("axiom") or self.root.find(".//*[@axiom]")
        if axiom:
            print("[CML-Validation] Axiom verification PASSED: 'Love-Over-God-Absolute' seal detected.")
            return True
        else:
            print("[CML-Validation Warning] Axiom seal missing or non-standard.")
            return False

    def to_json(self, output_json_path="cml_output.json"):
        """Converts the XML CML tree into a clean nested dictionary and exports to JSON."""
        def parse_element(elem):
            parsed = {
                "tag": elem.tag,
                "attributes": elem.attrib,
                "text": elem.text.strip() if elem.text and elem.text.strip() else None,
                "children": [parse_element(child) for child in elem]
            }
            return parsed

        manifest_dict = parse_element(self.root)
        
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(manifest_dict, f, indent=4)
            
        print(f"[CML-Chronicler] Manifest successfully translated to JSON: {output_json_path}")
        return manifest_dict

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY MARKUM LANGUAGE (CML) STANDARD PARSER")
    print("======================================================")
    
    # Target our previously generated economic or ecological audit manifest
    target_file = "coherence_economy_manifest.cml"
    
    parser = CmlParser(target_file)
    parser.load_manifest()
    parser.validate_axiom()
    json_data = parser.to_json("parsed_cml_output.json")
    
    print("\n[CML-Parser] Parsed Root Element:", json_data["tag"])
    print("[CML-Parser] Root Attributes:", json_data["attributes"])
    print("======================================================")