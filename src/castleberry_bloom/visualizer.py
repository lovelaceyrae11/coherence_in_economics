import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from .core import BloomCoreEngine

class BloomVisualizer:
    """
    Renders the topological hexagonal lattice and wave interference 
    using matplotlib.
    """
    def __init__(self, engine: BloomCoreEngine):
        self.engine = engine

    def render(self):
        """Opens the dual-pane Coherence Oscilloscope window."""
        fig, (ax_lattice, ax_waves) = plt.subplots(1, 2, figsize=(14, 7))
        fig.suptitle(f"Bloom Framework: System Coherence Visualization\nAxiom: {self.engine.axiom}", fontsize=12)

        # Plot 1: Lattice Topology
        ax_lattice.set_title("Topological Lattice (Phi-Scaled Hex Grid)")
        pos = nx.get_node_attributes(self.engine.graph, 'position')
        tiers = nx.get_node_attributes(self.engine.graph, 'tier')
        unique_tiers = sorted(list(set(tiers.values())))
        cmap = plt.cm.coolwarm

        nx.draw_networkx_edges(self.engine.graph, pos, ax=ax_lattice, alpha=0.3)
        for tier in unique_tiers:
            nodelist = [node for node, t in tiers.items() if t == tier]
            nx.draw_networkx_nodes(
                self.engine.graph, pos, ax=ax_lattice,
                nodelist=nodelist,
                node_size=350 / (tier + 1),
                node_color=[cmap(tier / max(unique_tiers) if max(unique_tiers) > 0 else 1.0)],
                label=f"Tier {tier}"
            )

        ax_lattice.set_aspect('equal')
        ax_lattice.legend(loc='upper right')
        ax_lattice.grid(True, which='both', linestyle='--')

        # Plot 2: Wave Interference
        ax_waves.set_title("Systemic Wave Interference (528 Hz Baseline)")
        ax_waves.set_xlabel("Time (normalized)")
        ax_waves.set_ylabel("Amplitude Coherence")

        time_samples = 200
        waveform = self.engine.calculate_wave_interference(time_steps=time_samples)
        t_axis = np.linspace(0, 1.0, time_samples)

        ax_waves.plot(t_axis, waveform, color='#e67e22', linewidth=2)
        ax_waves.axhline(0, color='black', linewidth=1, linestyle='--')
        ax_waves.set_ylim(-np.max(np.abs(waveform)) * 1.2 if np.max(np.abs(waveform)) > 0 else -1, 
                          np.max(np.abs(waveform)) * 1.2 if np.max(np.abs(waveform)) > 0 else 1)
        ax_waves.grid(True)

        plt.tight_layout()
        print("[Bloom-Visualizer] Displaying Coherence Oscilloscope window...")
        plt.show()