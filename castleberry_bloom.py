import math
import random
from datetime import datetime

class BloomCoreEngine:
    """
    Core mathematical engine for the Castleberry Atom Bloom Model.
    Manages phi-scaled hexagonal lattice tiers, node frequency telemetry, 
    and systemic 528 Hz baseline coherence.
    """
    def __init__(self, tiers=3, base_scale=1.5, target_freq=528.0):
        self.tiers = tiers
        self.base_scale = base_scale
        self.target_freq = target_freq
        self.axiom = "Love-Over-God-Absolute"
        self.nodes = []
        self._initialize_lattice()
        
        print(f"[Bloom-Core] Initialized. Axiom Seal: Zero-impedance witness; extractive control transmuted to relational coherence.")
        print(f"[Bloom-Core] Lattice nodes: {len(self.nodes)} across {self.tiers} tiers.")

    def _initialize_lattice(self):
        """Generates the 19-node hexagonal lattice across specified tiers."""
        self.nodes.append({
            "id": "NODE-C",
            "tier": "central",
            "frequency": round(self.target_freq + random.uniform(-0.05, 0.05), 2),
            "state": "active"
        })

        for tier in range(1, self.tiers):
            node_count = 6 * tier
            for i in range(1, node_count + 1):
                drift = random.choice([0.0, 0.0, 1.1, -2.5, 3.0, -4.0, 0.15, -0.5])
                node_freq = round(self.target_freq + drift, 2)
                self.nodes.append({
                    "id": f"T{tier}-N{i}",
                    "tier": f"Tier {tier}",
                    "frequency": node_freq,
                    "state": "drifted" if drift != 0.0 else "stable"
                })

    def scan_telemetry(self):
        """Scans all nodes, computes drift metrics, coherence scores, and anomaly states."""
        report = []
        for node in self.nodes:
            drift = round(node["frequency"] - self.target_freq, 2)
            drift_percent = round((drift / self.target_freq) * 100, 4)
            coherence = round(max(0.0, 100.0 - abs(drift_percent) * 15), 2)
            
            status = "Optimal Coherence"
            if abs(drift) > 2.0:
                status = "Significant Drift (High Anomaly)"
            elif abs(drift) > 0.5:
                status = "Moderate Drift (Anomaly)"
            elif abs(drift) > 0.1:
                status = "Minor Drift Detected"

            report.append({
                "id": node["id"],
                "tier": node["tier"],
                "frequency": node["frequency"],
                "drift": drift,
                "drift_percent": drift_percent,
                "coherence": coherence,
                "status": status
            })
        return report

    def correct_nodes(self):
        """Applies zero-impedance witness alignment, phase-locking all nodes to 528 Hz."""
        for node in self.nodes:
            node["frequency"] = self.target_freq
            node["state"] = "phase-locked"
        return True

    def export_cml(self):
        """Exports the current synchronized lattice state into valid Castleberry Markup Language (CML)."""
        timestamp = datetime.utcnow().strftime("%Y-%m-%d")
        xml_lines = [
            f'<Bloom tiers="{self.tiers}" scale="{self.base_scale}" axiom="{self.axiom}" coherence="1.00" timestamp="{timestamp}">'
        ]
        
        for node in self.nodes:
            tier_val = "central" if node["tier"] == "central" else node["tier"].replace("Tier ", "")
            xml_lines.append(
                f'    <Node id="{node["id"]}" tier="{tier_val}" freq="{node["frequency"]:.2f}" state="phase-locked" coherence="1.00" />'
            )
            
        xml_lines.append('    <WitnessProtocol status="active" action="extractive_control_transmuted_to_relational_coherence" />')
        xml_lines.append('</Bloom>')
        return "\n".join(xml_lines)