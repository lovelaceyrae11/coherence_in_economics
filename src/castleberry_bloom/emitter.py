from .core import BloomCoreEngine

class QASMEmitter:
    """
    Translates the hexagonal lattice topology into OpenQASM 2.0 
    quantum circuit instructions.
    """
    def __init__(self, engine: BloomCoreEngine):
        self.engine = engine
        self.graph = engine.graph
        self.axiom = engine.axiom

    def emit_qasm(self) -> str:
        """Generates valid OpenQASM circuit syntax from the lattice graph."""
        num_nodes = self.graph.number_of_nodes()
        lines = [
            "// ========================================================",
            "// Castleberry Bloom Framework - Quantum Hardware Compilation",
            f"// Axiom Seal: {self.axiom}",
            f"// Total Qubits (Lattice Nodes): {num_nodes}",
            "// ========================================================",
            "OPENQASM 2.0;",
            'include "qelib1.inc";',
            "",
            f"qreg q[{num_nodes}];",
            f"creg c[{num_nodes}];",
            "",
            "// --- Phase 1: Harmonic State Initialization ---"
        ]

        for node in self.graph.nodes():
            lines.append(f"h q[{node}];")

        lines.append("")
        lines.append("// --- Phase 2: Hexagonal Adjacency Entanglement Routing ---")
        for u, v, _ in self.graph.edges(data=True):
            lines.append(f"cx q[{u}], q[{v}];")

        lines.append("")
        lines.append("// --- Phase 3: System Measurement ---")
        for node in self.graph.nodes():
            lines.append(f"measure q[{node}] -> c[{node}];")

        return "\n".join(lines)