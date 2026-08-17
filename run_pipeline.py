from castleberry_bloom import CMLCompiler, BloomOrchestrator, QASMEmitter, BloomVisualizer

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY BLOOM ENTERPRISE FRAMEWORK - PIPELINE RUN")
    print("======================================================")

    # 1. Ingest via Castleberry Markup Language (CML)
    sample_cml = """
    <Bloom tiers="3" scale="1.5" axiom="Love-Over-God-Absolute">
        <Node id="origin" freq="528.0" state="cooperant" />
    </Bloom>
    """
    compiler = CMLCompiler(sample_cml)
    engine = compiler.parse()

    # 2. Run Multi-Agent Telemetry & Harmonic Correction
    orchestrator = BloomOrchestrator(engine, num_agents=3)
    orchestrator.execute_telemetry_cycle(cycles=2)

    # 3. Compile to Quantum Hardware (OpenQASM)
    emitter = QASMEmitter(engine)
    qasm_code = emitter.emit_qasm()
    print("--- Generated OpenQASM Output Sample ---")
    print("\n".join(qasm_code.splitlines()[:12]))
    print("... [Circuit compilation complete] ...\n")

    # 4. Render Visual Coherence Oscilloscope
    visualizer = BloomVisualizer(engine)
    visualizer.render()