# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def generate_blueprint(frequency=528.0, rings=8):
    print(f"[Pointillism-Engine] Calculating golden-ratio lattice for {frequency} Hz...")
    
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    
    for i in range(1, rings + 1):
        radius = (phi ** i) * 0.1
        num_dots = int(6 * i * (frequency / 528.0))
        theta = np.linspace(0, 2 * np.pi, num_dots, endpoint=False)
        r = np.full_like(theta, radius)
        
        ax.scatter(theta, r, s=max(20, 150 - i*12), c='#58a6ff', alpha=0.8, edgecolors='#ffffff', linewidths=0.5)

    ax.set_axis_off()
    plt.title(f"Castleberry Bloom: Pointillism Blueprint ({frequency} Hz)", color='#ffffff', fontsize=12, pad=20)
    
    filename = f"blueprint_{int(frequency)}hz.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    
    print(f"[Pointillism-Engine] Blueprint saved successfully as '{filename}'!")

if __name__ == "__main__":
    generate_blueprint(528.0, 9)
