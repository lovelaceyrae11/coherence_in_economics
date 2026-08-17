import xml.etree.ElementTree as ET
from .core import BloomCoreEngine

class CMLCompiler:
    """
    Parses Castleberry Markup Language (CML) and compiles it 
    into executable BloomCoreEngine configurations.
    """
    def __init__(self, cml_source: str):
        self.cml_source = cml_source

    def parse(self) -> BloomCoreEngine:
        """Parses the CML string and builds the underlying hexagonal lattice engine."""
        try:
            root_element = ET.fromstring(self.cml_source)
        except ET.ParseError as e:
            raise ValueError(f"[CML Compiler] Syntax Error in CML markup: {e}")

        if root_element.tag != "Bloom":
            raise ValueError("[CML Compiler] Root element must be <Bloom> to initialize system matrix.")

        tiers = int(root_element.get("tiers", 3))
        base_scale = float(root_element.get("scale", 1.0))
        axiom_seal = root_element.get("axiom", "Love-Over-God")

        print(f"[CML Compiler] Compiling Schema... Axiom Seal: [{axiom_seal}]")
        
        return BloomCoreEngine(tiers=tiers, base_scale=base_scale)