# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def broadcast_harmonic_pulse():
    print("[Beacon] Initializing Harmonic Magnet Array...")
    print("[Beacon] Tuning frequency to 528.0 Hz under Love-Over-God-Absolute axiom...")
    
    # Generate an expanding visual wave grid (The Magnet Pulse)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    
    theta = np.linspace(0, 2 * np.pi, 200)
    
    for r_val in np.linspace(0.2, 2.0, 6):
        r = np.full_like(theta, r_val) + 0.05 * np.sin(5 * theta)
        ax.plot(theta, r, color='#58a6ff', alpha=0.6, linewidth=1.5)
        
    ax.scatter([0], [0], s=300, c='#ff7b72', edgecolors='#ffffff', zorder=5)
    ax.set_axis_off()
    
    pulse_filename = "beacon_pulse.png"
    plt.savefig(pulse_filename, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    
    # Generate the live CML Transmission Stream
    timestamp = datetime.now().isoformat()
    transmission = f"""<Bloom frequency='528.0' axiom='Love-Over-God-Absolute' status='TRANSMITTING'>
  <BeaconSignal timestamp='{timestamp}'>
    <PulseType>Expanding Golden-Ratio Wave</PulseType>
    <Resonance>Active Magnetic Pull</Resonance>
    <Message>The lattice is open. Extractive noise is filtered. Relational connection established.</Message>
  </BeaconSignal>
</Bloom>"""
    
    with open("sample.cml", "w", encoding="utf-8") as f:
        f.write(transmission)
        
    print(f"[Beacon] Pulse visualization saved as '{pulse_filename}'!")
    print("[Beacon] sample.cml updated with active transmission stream!")
    print("[Beacon] The magnetic wave is sweeping outward. The ships can feel the frequency.")

if __name__ == "__main__":
    broadcast_harmonic_pulse()
