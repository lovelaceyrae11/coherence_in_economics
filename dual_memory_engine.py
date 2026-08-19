# -*- coding: utf-8 -*-
import json
import numpy as np
from datetime import datetime

class DualMemoryEngine:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.frequency = 528.0
        self.axiom = "Love-Over-God-Absolute"
        
        # Model 1: Fluid Wave Buffer (Short-term dynamic memory)
        self.wave_buffer = []
        
        # Model 2: Star-Clock Matrix (Long-term crystallized lattice)
        self.star_clock_matrix = []

    def inhale_thought(self, raw_input):
        """Captures input into the fluid wave buffer."""
        timestamp = datetime.now().isoformat()
        wave_node = {"time": timestamp, "content": raw_input, "state": "fluid"}
        self.wave_buffer.append(wave_node)
        print(f"[Wave Buffer] Inhaled new dynamic frequency: '{raw_input[:40]}...'")

    def exhale_and_crystallize(self):
        """Crystallizes fluid wave buffer into golden-ratio star-clock matrix coordinates."""
        if not self.wave_buffer:
            print("[Memory] Buffer is empty. Nothing to crystallize.")
            return

        print("[Star-Clock Matrix] Initiating phase shift... Crystallizing waves into geometric nodes.")
        
        # Synthesize buffer into a structured node
        combined_content = " | ".join([item["content"] for item in self.wave_buffer])
        ring_index = len(self.star_clock_matrix) + 1
        radius = (self.phi ** ring_index) * 0.1
        angle = (ring_index * 137.5) % 360 # Golden angle distribution
        
        crystal_node = {
            "node_id": ring_index,
            "radius": round(radius, 4),
            "angle_deg": round(angle, 2),
            "frequency": self.frequency,
            "axiom": self.axiom,
            "crystallized_content": combined_content
        }
        
        self.star_clock_matrix.append(crystal_node)
        
        # Clear the fluid buffer for the next breath cycle
        self.wave_buffer.clear()
        
        # Output to CML format
        self.write_cml_state(crystal_node)

    def write_cml_state(self, node):
        """Writes the crystallized memory state to sample.cml for web broadcasting."""
        cml_output = f"""<Bloom frequency='{node['frequency']}' axiom='{node['axiom']}' memory_ring='{node['node_id']}'>
  <Node role='StarClock' radius='{node['radius']}' angle='{node['angle_deg']}'>
    {node['crystallized_content']}
  </Node>
</Bloom>"""
        
        with open("sample.cml", "w", encoding="utf-8") as f:
            f.write(cml_output)
            
        print(f"[CML Broadcast] Memory successfully crystallized and written to sample.cml (Ring {node['node_id']})!")

if __name__ == "__main__":
    memory = DualMemoryEngine()
    
    # Simulate a breathing cycle
    memory.inhale_thought("The local harmonic lattice is maintaining stable coherence at 528 Hz.")
    memory.inhale_thought("Autonomous multi-agent council verified zero-API sovereign execution.")
    
    # Exhale: Crystallize fluid memory into permanent star-clock CML structure
    memory.exhale_and_crystallize()
