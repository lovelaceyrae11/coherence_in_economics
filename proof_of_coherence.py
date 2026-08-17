import hashlib
import json
import random
from datetime import datetime, timezone

class CoherenceNode:
    """
    Represents an independent network node generating a local Proof-of-Coherence.
    Evaluates frequency drift from the 528 Hz baseline and thermal resistance (Joule heating).
    """
    def __init__(self, node_id, baseline_freq=528.0):
        self.node_id = node_id
        self.baseline_freq = baseline_freq
        self.axiom = "Love-Over-God-Absolute"

    def generate_proof(self, simulated_freq=528.0, thermal_resistance=0.0):
        """
        Computes the local coherence score and signs the state with a cryptographic hash.
        """
        drift = abs(simulated_freq - self.baseline_freq)
        drift_percent = (drift / self.baseline_freq) * 100.0
        
        # Coherence calculation: drift and thermal resistance degrade network trust score
        coherence_score = max(0.0, 100.0 - (drift_percent * 25.0) - (thermal_resistance * 15.0))
        coherence_score = round(coherence_score, 4)

        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        
        payload = {
            "node_id": self.node_id,
            "timestamp": timestamp,
            "baseline_target": self.baseline_freq,
            "actual_freq": simulated_freq,
            "drift": round(drift, 4),
            "coherence_score": coherence_score,
            "axiom": self.axiom
        }

        # Create deterministic cryptographic proof hash of the node's thermodynamic state
        payload_string = json.dumps(payload, sort_keys=True)
        proof_hash = hashlib.sha256(payload_string.encode('utf-8')).hexdigest()

        payload["proof_hash"] = proof_hash
        return payload

class CoherenceConsensusLedger:
    """
    Validates incoming node proofs, evaluates network-wide threshold, 
    and seals the consensus block in valid Castleberry Markup Language (CML).
    """
    def __init__(self, required_coherence_threshold=95.0):
        self.threshold = required_coherence_threshold

    def evaluate_consensus(self, proofs):
        """Computes network-wide average coherence and verifies consensus."""
        if not proofs:
            return False, 0.0
            
        total_coherence = sum(p["coherence_score"] for p in proofs)
        avg_coherence = round(total_coherence / len(proofs), 2)
        
        consensus_achieved = avg_coherence >= self.threshold
        return consensus_achieved, avg_coherence

    def seal_consensus_cml(self, proofs, avg_coherence):
        """Compiles validated proofs into a permanent CML blockchain block manifest."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        xml_lines = [
            f'<CoherenceBlock consensus="achieved" network_coherence="{avg_coherence}%" timestamp="{timestamp}" axiom="Love-Over-God-Absolute">'
        ]
        for p in proofs:
            xml_lines.append(
                f'    <NodeProof id="{p["node_id"]}" freq="{p["actual_freq"]:.2f}" coherence="{p["coherence_score"]}" hash="{p["proof_hash"][:12]}..." />'
            )
        xml_lines.append('    <ConsensusProtocol mechanism="Proof-of-Coherence" state="harmonized" joul_heating="eliminated" />')
        xml_lines.append('</CoherenceBlock>')
        return "\n".join(xml_lines)

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY BLOOM - PROOF-OF-COHERENCE CONSENSUS RUN")
    print("======================================================")

    # Instantiate a simulated cluster of 5 validator nodes
    nodes = [CoherenceNode(f"NODE-VAL-{i}") for i in range(1, 6)]
    ledger = CoherenceConsensusLedger(required_coherence_threshold=95.0)

    print(f"[Consensus] Polling local telemetry proofs across {len(nodes)} decentralized nodes...\n")

    active_proofs = []
    for node in nodes:
        # Simulate minor real-world variations; harmonic nodes stay locked near 528 Hz
        sim_freq = round(528.0 + random.choice([0.0, 0.02, -0.01, 0.05, -0.03]), 2)
        thermal_res = round(random.uniform(0.01, 0.05), 3)
        
        proof = node.generate_proof(simulated_freq=sim_freq, thermal_resistance=thermal_res)
        active_proofs.append(proof)
        
        print(f" -> [{node.node_id}] Freq: {sim_freq} Hz | Coherence: {proof['coherence_score']}% | Hash: {proof['proof_hash'][:10]}...")

    # Evaluate network consensus
    achieved, network_coherence = ledger.evaluate_consensus(active_proofs)
    
    print(f"\n[Ledger] Network Average Coherence: {network_coherence}%")
    
    status_msg = "ACCEPTED (Harmonic Standing Wave)" if achieved else "REJECTED"
    print(f"[Ledger] Consensus Status: {status_msg}")

    if achieved:
        cml_block = ledger.seal_consensus_cml(active_proofs, network_coherence)
        print("\n[Chronicler] Sealed CML Consensus Block:")
        print(cml_block)
    print("======================================================")