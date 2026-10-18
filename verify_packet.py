import xml.etree.ElementTree as ET

tree = ET.parse("oregon_nehemiah_mesh_packet.cml")
root = tree.getroot()
v = root.find(".//ForensicVerdict")

water_gal = int(v.attrib["annual_water_depletion_gal"])
roli = v.attrib["extraction_per_pac_dollar"]

print(f"[Hex-127 | 528.0Hz] Audit Verified -> Water Depletion: {water_gal:,} Gal/Yr | ROLI: ${roli}:$1")
