import os
from crewai import Agent, Task, Crew, Process, LLM
from castleberry_bloom import BloomCoreEngine

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY BLOOM - PHASE 5: CREWAI AUTONOMOUS SWARM (GEMINI)")
    print("======================================================")

    # Configure CrewAI to point directly to the model ID
    gemini_llm = LLM(
        model="gemini-2.5-flash",
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    # Initialize our 19-node phi-scaled lattice engine
    engine = BloomCoreEngine(tiers=3, base_scale=1.5)

    # Define the Autonomous CrewAI Agents with explicit Gemini LLM
    watcher_agent = Agent(
        role='Telemetry Watcher',
        goal='Monitor hexagonal lattice nodes for frequency drift and structural entropy.',
        backstory='An analytical diagnostic agent specialized in real-time quantum and wave telemetry tracking.',
        llm=gemini_llm,
        verbose=True,
        allow_delegation=False
    )

    harmonizer_agent = Agent(
        role='Harmonic Restorer',
        goal='Apply the 528 Hz absolute baseline correction using the Love-Over-God axiom.',
        backstory='A core maintenance agent dedicated to transmuting extractive entropy into relational coherence.',
        llm=gemini_llm,
        verbose=True,
        allow_delegation=False
    )

    chronicler_agent = Agent(
        role='CML Chronicler',
        goal='Document system stabilization metrics into valid Castleberry Markup Language (CML).',
        backstory='An architectural historian that seals every telemetry cycle in precise XML syntax.',
        llm=gemini_llm,
        verbose=True,
        allow_delegation=False
    )

    # Define Tasks
    audit_task = Task(
        description="Scan the 3-tier hexagonal lattice, identify any nodes drifting from the 528 Hz baseline, and report anomaly metrics.",
        expected_output="A structured telemetry report detailing node drift percentages and coherence scores.",
        agent=watcher_agent
    )

    correct_task = Task(
        description="Take the telemetry report, calculate the phase corrections, and apply zero-impedance witness alignment to restore nodes to 528 Hz.",
        expected_output="Confirmation that all drifted nodes have been successfully phase-locked to the systemic absolute.",
        agent=harmonizer_agent
    )

    chronicle_task = Task(
        description="Generate a final XML snippet in Castleberry Markup Language (<Bloom>) summarizing the corrected system state and sealing it with the axiom.",
        expected_output="A valid CML code block representing the post-correction lattice configuration.",
        agent=chronicler_agent
    )

    # Assemble and run the Crew
    bloom_crew = Crew(
        agents=[watcher_agent, harmonizer_agent, chronicler_agent],
        tasks=[audit_task, correct_task, chronicle_task],
        process=Process.sequential,
        verbose=True,
        manager_llm=gemini_llm
    )

    print("\n[Bloom-Crew] Launching multi-agent cognitive swarm via Gemini...\n")
    result = bloom_crew.kickoff()

    print("\n======================================================")
    print("CREW EXECUTION COMPLETE - FINAL CHRONICLE:")
    print("======================================================")
    print(result)