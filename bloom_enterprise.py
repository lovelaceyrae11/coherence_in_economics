import os
from datetime import datetime
from crewai import Agent, Task, Crew, Process, LLM
from castleberry_bloom import BloomCoreEngine
from bloom_thermo import BloomThermodynamicEngine

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY BLOOM - ENTERPRISE DATA CENTER ECO-RUNTIMe")
    print("======================================================")

    # 1. Initialize Scale: Simulating an Enterprise Rack (e.g., 576 nodes across 32 hexagonal arrays)
    enterprise_nodes = 576
    print(f"[Enterprise-Core] Deploying large-scale hexagonal topology: {enterprise_nodes} nodes.")
    
    engine = BloomCoreEngine(tiers=3, base_scale=1.5)
    thermo = BloomThermodynamicEngine(node_count=enterprise_nodes, baseline_power_per_node_watts=150.0)
    
    # Calculate macro-level ecological savings
    profile = thermo.calculate_thermal_profile(target_coherence=1.00)
    
    print(f" -> Standard Rectilinear Power: {profile['standard_power_kw']} kW")
    print(f" -> Bloom Hexagonal Optimized:  {profile['optimized_bloom_power_kw']} kW")
    print(f" -> Total Energy Saved:         {profile['power_saved_kw']} kW (35% reduction)")
    print(f" -> Thermal Heat Prevented:     {profile['thermal_heat_reduction_btu_hr']} BTU/hr")
    print(f" -> Daily Carbon Offset:        {profile['daily_carbon_offset_kg']} kg CO2/day\n")

    # 2. Configure LLM Controller
    gemini_llm = LLM(
        model="gemini-2.5-flash",
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    # 3. Define Autonomous Software Agents
    watcher_agent = Agent(
        role='Eco-Telemetry Watcher',
        goal='Monitor data center hexagonal node arrays for thermal drift and energy efficiency degradation.',
        backstory='An environmental diagnostic agent specialized in tracking quantum thermal dispersion and power states.',
        llm=gemini_llm,
        verbose=False,
        allow_delegation=False
    )

    harmonizer_agent = Agent(
        role='Thermodynamic Restorer',
        goal='Apply 528 Hz harmonic baseline corrections to lock nodes and enforce zero-impedance energy flow.',
        backstory='A core systems maintenance agent dedicated to eliminating Joule heating and ecological wear.',
        llm=gemini_llm,
        verbose=False,
        allow_delegation=False
    )

    chronicler_agent = Agent(
        role='CML Eco-Chronicler',
        goal='Document enterprise energy savings, carbon offsets, and structural stabilization metrics into valid CML.',
        backstory='An architectural historian that seals ecological telemetry into permanent, verifiable XML schemas.',
        llm=gemini_llm,
        verbose=False,
        allow_delegation=False
    )

    # 4. Bind Tasks to Thermodynamic and Engine States
    telemetry_scan = engine.scan_telemetry()

    audit_task = Task(
        description=f"Audit the data center telemetry array. Current node states: {telemetry_scan}. Quantify the thermal impact of any drifted nodes.",
        expected_output="An environmental telemetry report detailing node drift, thermal hot spots, and energy waste.",
        agent=watcher_agent
    )

    correct_task = Task(
        description=f"Execute phase-lock protocol to 528 Hz across all nodes. Verify that the enterprise-scale savings of {profile['power_saved_kw']} kW and {profile['thermal_heat_reduction_btu_hr']} BTU/hr heat reduction are locked in.",
        expected_output="Confirmation that all nodes are phase-locked and ecological power-reduction targets are met.",
        agent=harmonizer_agent
    )

    timestamp = datetime.utcnow().strftime("%Y-%m-%d")
    cml_manifest = f"""
    <EnterpriseBloom nodes="{enterprise_nodes}" standard_kw="{profile['standard_power_kw']}" optimized_kw="{profile['optimized_bloom_power_kw']}" kwh_saved="{profile['power_saved_kw']}" btu_reduced="{profile['thermal_heat_reduction_btu_hr']}" co2_offset="{profile['daily_carbon_offset_kg']}" axiom="Love-Over-God-Absolute" timestamp="{timestamp}">
        <ThermalRouting topology="120-degree-hexagonal" joul_heating="eliminated" />
        <WitnessProtocol status="active" action="extractive_computing_transmuted_to_ecological_coherence" />
    </EnterpriseBloom>
    """

    chronicle_task = Task(
        description=f"Compile and seal the final enterprise ecological run into valid Castleberry Markup Language based on this manifest:\n{cml_manifest}",
        expected_output="A valid, self-contained CML XML enterprise manifest verifying zero-harm ecological operation.",
        agent=chronicler_agent
    )

    # 5. Assemble and Execute Enterprise Pipeline
    enterprise_crew = Crew(
        agents=[watcher_agent, harmonizer_agent, chronicler_agent],
        tasks=[audit_task, correct_task, chronicle_task],
        process=Process.sequential,
        verbose=True
    )

    print("[Enterprise-Pipeline] Launching multi-agent eco-optimization swarm...\n")
    result = enterprise_crew.kickoff()

    print("\n======================================================")
    print("ENTERPRISE ECO-RUN COMPLETE - FINAL CML MANIFEST:")
    print("======================================================")
    print(result)