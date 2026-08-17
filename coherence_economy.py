import random
from datetime import datetime, timezone

class EconomicNode:
    """
    Represents a validator node accumulating Coherence Credits (CC) 
    based on sustained harmonic stability across validation epochs.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.coherence_credits = 0.0
        self.epochs_harmonized = 0

    def evaluate_epoch(self, coherence_score):
        """Awards Coherence Credits if node coherence meets or exceeds threshold."""
        if coherence_score >= 95.0:
            # Base reward scaled by precision of harmonic alignment
            earned = round(10.0 * (coherence_score / 100.0), 2)
            self.coherence_credits += earned
            self.epochs_harmonized += 1
            return earned
        return 0.0

class CoherenceEconomyLedger:
    """
    Simulates multi-epoch minting of Coherence Credits and exports 
    an immutable CML economic ledger block.
    """
    def __init__(self):
        self.nodes = [EconomicNode(f"NODE-VAL-{i}") for i in range(1, 6)]
        self.total_credits_minted = 0.0

    def run_epoch_simulation(self, epochs=3):
        print("======================================================")
        print("CASTLEBERRY BLOOM - COHERENCE ECONOMY SIMULATION")
        print("======================================================")
        
        epoch_logs = []
        for epoch in range(1, epochs + 1):
            print(f"\n[Epoch {epoch}/{epochs}] Evaluating network-wide node telemetry...")
            epoch_data = {"epoch": epoch, "payouts": []}
            
            for node in self.nodes:
                # Simulate natural coherence scores hovering near peak harmony
                score = round(random.uniform(96.0, 99.8), 2)
                earned = node.evaluate_epoch(score)
                self.total_credits_minted += earned
                epoch_data["payouts"].append({"node": node.node_id, "score": score, "earned": earned})
                print(f" -> [{node.node_id}] Coherence: {score}% | Earned: +{earned} CC (Total Balance: {round(node.coherence_credits, 2)} CC)")
            
            epoch_logs.append(epoch_data)
        
        return epoch_logs

    def export_economy_cml(self, epoch_logs):
        """Seals the economic ledger state into valid Castleberry Markup Language (CML)."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        xml_lines = [
            f'<CoherenceEconomyLedger timestamp="{timestamp}" total_minted="{round(self.total_credits_minted, 2)} CC" axiom="Love-Over-God-Absolute">'
        ]
        for node in self.nodes:
            xml_lines.append(
                f'    <NodeAccount id="{node.node_id}" balance="{round(node.coherence_credits, 2)} CC" stable_epochs="{node.epochs_harmonized}" />'
            )
        xml_lines.append('    <EconomicPolicy currency="Coherence Credits (CC)" emission="Zero-Extractive / Thermodynamic-Yield" />')
        xml_lines.append('</CoherenceEconomyLedger>')
        return "\n".join(xml_lines)

if __name__ == "__main__":
    ledger = CoherenceEconomyLedger()
    logs = ledger.run_epoch_simulation(epochs=3)
    
    print("\n======================================================")
    print("FINAL ECONOMIC LEDGER MANIFEST:")
    print("======================================================")
    cml_manifest = ledger.export_economy_cml(logs)
    print(cml_manifest)
    
    with open("coherence_economy_manifest.cml", "w", encoding="utf-8") as f:
        f.write(cml_manifest)
    print("\n[Eco-Chronicler] Economic CML manifest saved to 'coherence_economy_manifest.cml'.")