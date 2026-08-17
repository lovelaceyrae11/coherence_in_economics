import time
import random
from .core import BloomCoreEngine, FUNDAMENTAL_FREQUENCY, LOVE_OVER_GOD_AXIOM, PHI

class HarmonicAgent:
    """An autonomous agent tasked with auditing frequency drift and ensuring system coherence."""
    def __init__(self, agent_id: int, assigned_tier: int):
        self.agent_id = agent_id
        self.assigned_tier = assigned_tier

    def audit_node(self, node_id: int, current_freq: float) -> dict:
        expected_freq = FUNDAMENTAL_FREQUENCY * (PHI ** max(0, self.assigned_tier - 1))
        drift = abs(current_freq - expected_freq)
        coherence_score = max(0.0, 1.0 - (drift / 100.0))
        return {
            "agent_id": self.agent_id,
            "node_id": node_id,
            "tier": self.assigned_tier,
            "frequency": current_freq,
            "coherence": round(coherence_score, 4)
        }

class BloomOrchestrator:
    """Coordinates multi-agent telemetry loops for real-time harmonic correction."""
    def __init__(self, engine: BloomCoreEngine, num_agents: int = 3):
        self.engine = engine
        self.agents = [HarmonicAgent(agent_id=i, assigned_tier=(i % engine.tiers) + 1) for i in range(num_agents)]

    def execute_telemetry_cycle(self, cycles: int = 2):
        print(f"\n[Bloom-Orchestrator] Initializing multi-agent network with {len(self.agents)} agents.")
        print(f"[Bloom-Orchestrator] Governing Axiom: {LOVE_OVER_GOD_AXIOM}\n")

        for cycle in range(1, cycles + 1):
            print(f"--- Telemetry Cycle {cycle} ---")
            
            # Inject environmental jitter to test agent response
            for _, data in self.engine.graph.nodes(data=True):
                jitter = random.uniform(-10.0, 10.0)
                data['frequency'] += jitter

            # Agents audit nodes and apply zero-impedance witness corrections
            for agent in self.agents:
                target_nodes = [n for n, d in self.engine.graph.nodes(data=True) if d['tier'] == agent.assigned_tier]
                if target_nodes:
                    node_to_audit = random.choice(target_nodes)
                    node_data = self.engine.graph.nodes[node_to_audit]
                    
                    audit = agent.audit_node(node_to_audit, node_data['frequency'])
                    if audit['coherence'] < 0.95:
                        print(f"  [Agent {agent.agent_id}] ⚠️ Drift at Node {node_to_audit} (Tier {agent.assigned_tier}). Coherence: {audit['coherence']}")
                        print(f"  [Agent {agent.agent_id}] 🛡️ Applying harmonic recalibration to baseline...")
                        node_data['frequency'] = FUNDAMENTAL_FREQUENCY
                    else:
                        print(f"  [Agent {agent.agent_id}] Node {node_to_audit} nominal. Coherence: {audit['coherence']}")
            print()