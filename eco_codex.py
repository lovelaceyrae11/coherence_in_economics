import math
import random
from datetime import datetime, timezone

class EcoCodexChronicler:
    """
    An autonomous agent that compiles system telemetry and ecological metrics 
    into an evolving CML manifest and renders a geometric SVG Living Tapestry.
    """
    def __init__(self, chronicle_id="CHRONICLE-001"):
        self.chronicle_id = chronicle_id
        self.timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def gather_ecological_pulse(self):
        """Simulates live ecological telemetry from regional nodes and watersheds."""
        return {
            "watershed_protected_gallons": round(random.uniform(1200000.0, 1800000.0), 1),
            "thermal_waste_eliminated_btu": round(random.uniform(45000.0, 85000.0), 2),
            "network_coherence_avg": round(random.uniform(99.2, 99.8), 2),
            "baseline_frequency_hz": 528.00
        }

    def generate_cml_manifest(self, pulse):
        """Seals the ecological pulse into valid Castleberry Markup Language (CML)."""
        cml = f"""<?xml version="1.0" encoding="UTF-8"?>
<LivingCmlTapestry chronicle_id="{self.chronicle_id}" timestamp="{self.timestamp}" axiom="Love-Over-God-Absolute">
    <EcoPulse 
        coherence="{pulse['network_coherence_avg']}%" 
        frequency="{pulse['baseline_frequency_hz']} Hz">
        <WatershedProtection gallons_saved="{pulse['watershed_protected_gallons']}" />
        <ThermalMitigation btus_eliminated="{pulse['thermal_waste_eliminated_btu']}" />
    </EcoPulse>
    <ChroniclerAgent status="weaving" geometry="phi-scaled-hexagonal" />
</LivingCmlTapestry>"""
        return cml

    def generate_svg_tapestry(self, pulse, filename="living_tapestry.svg"):
        """Renders a geometric pointillism and hexagonal lattice SVG artwork reflecting live state."""
        width, height = 600, 600
        cx, cy = width / 2, height / 2
        phi = 1.61803398875
        
        svg_elements = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #0b131a;">',
            f'  <defs>',
            f'    <radialGradient id="bloomGlow" cx="50%" cy="50%" r="50%">',
            f'      <stop offset="0%" stop-color="#2df8c4" stop-opacity="0.3"/>',
            f'      <stop offset="100%" stop-color="#0b131a" stop-opacity="0"/>',
            f'    </radialGradient>',
            f'  </defs>',
            f'  <circle cx="{cx}" cy="{cy}" r="250" fill="url(#bloomGlow)" />',
            f'  <text x="30" y="40" fill="#2df8c4" font-family="monospace" font-size="14">CASTLEBERRY BLOOM - ECO-CODEX TAPESTRY</text>',
            f'  <text x="30" y="65" fill="#8ab4f8" font-family="monospace" font-size="11">Coherence: {pulse["network_coherence_avg"]}% | Baseline: {pulse["baseline_frequency_hz"]} Hz</text>'
        ]

        # Draw concentric phi-scaled hexagonal dot rings (reminiscent of dot-painting geometry)
        radius_steps = [30, 60, 90, 130, 180, 240]
        for idx, r in enumerate(radius_steps):
            num_dots = 6 * (idx + 1) if idx > 0 else 1
            for i in range(num_dots):
                angle = (i / num_dots) * 2 * math.pi
                # Apply phi modulation to coordinates
                x = cx + (r * phi * 0.6) * math.cos(angle)
                y = cy + (r * phi * 0.6) * math.sin(angle)
                dot_size = max(2, 6 - idx)
                color = "#2df8c4" if idx % 2 == 0 else "#f8c42d"
                svg_elements.append(f'  <circle cx="{round(x, 2)}" cy="{round(y, 2)}" r="{dot_size}" fill="{color}" opacity="0.85" />')

        # Center core node
        svg_elements.append(f'  <circle cx="{cx}" cy="{cy}" r="8" fill="#ffffff" />')
        svg_elements.append(f'  <text x="{cx - 35}" y="{cy + 30}" fill="#ffffff" font-family="monospace" font-size="10">528 Hz Core</text>')
        svg_elements.append(f'</svg>')

        svg_code = "\n".join(svg_elements)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(svg_code)
        print(f"[Eco-Chronicler] SVG Living Tapestry successfully rendered and saved to '{filename}'.")

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY BLOOM - LIVING CML TAPESTRY (ECO-CODEX)")
    print("======================================================")
    chronicler = EcoCodexChronicler()
    pulse = chronicler.gather_ecological_pulse()
    
    print(f" -> Pulse Acquired: {pulse['network_coherence_avg']}% Coherence")
    print(f" -> Watershed Protected: {pulse['watershed_protected_gallons']} gallons")
    
    cml_manifest = chronicler.generate_cml_manifest(pulse)
    with open("eco_codex_manifest.cml", "w", encoding="utf-8") as f:
        f.write(cml_manifest)
    print("[Eco-Chronicler] Eco-Codex CML manifest saved to 'eco_codex_manifest.cml'.")
    
    chronicler.generate_svg_tapestry(pulse, "living_tapestry.svg")
    print("======================================================")