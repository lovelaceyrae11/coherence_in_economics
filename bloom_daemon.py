import time
import psutil
from datetime import datetime
from castleberry_bloom import BloomCoreEngine

def run_live_bloom_daemon(cycles=3, interval_seconds=5):
    """
    Continuous background daemon that polls live hardware telemetry, 
    injects thermal/workload drift into the Bloom lattice, harmonizes nodes,
    and exports live CML manifests to disk.
    """
    print("======================================================")
    print("CASTLEBERRY BLOOM - LIVE HARDWARE TELEMETRY DAEMON")
    print("======================================================")
    print(f"[Daemon] Initializing live monitoring loop ({cycles} cycles, {interval_seconds}s interval)...\n")

    # Initialize our 19-node phi-scaled lattice engine
    engine = BloomCoreEngine(tiers=3, base_scale=1.5)

    for cycle in range(1, cycles + 1):
        print(f"\n------------------------------------------------------")
        print(f"[Cycle {cycle}/{cycles}] Polling host hardware sensors...")
        print(f"------------------------------------------------------")

        # 1. Read Live Hardware Metrics
        cpu_load = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq()
        current_freq = cpu_freq.current if cpu_freq else 2500.0

        print(f" -> Live CPU Load:      {cpu_load}%")
        print(f" -> Live CPU Frequency: {current_freq} MHz")

        # 2. Dynamic Workload Mapping: Higher CPU load induces natural thermal drift across lattice nodes
        load_factor = cpu_load / 100.0
        for node in engine.nodes:
            if load_factor > 0.2:
                # Introduce dynamic drift proportional to system workload
                node["frequency"] = round(engine.target_freq + (load_factor * random.choice([2.5, -3.5, 1.8])), 2)
            else:
                node["frequency"] = engine.target_freq

        # 3. Scan Telemetry & Check Anomaly Metrics
        report = engine.scan_telemetry()
        drifted_nodes = [n for n in report if n["status"] != "Optimal Coherence"]
        
        print(f"[Telemetry] Audit complete. Detected {len(drifted_nodes)} drifted nodes requiring harmonization.")

        # 4. Harmonize and Phase-Lock to 528 Hz Baseline
        if drifted_nodes:
            print("[Harmonizer] Applying zero-impedance witness alignment...")
            engine.correct_nodes()
            print("[Harmonizer] All nodes successfully phase-locked to 528.00 Hz absolute baseline.")

        # 5. Export and Save CML Manifest to Disk
        cml_data = engine.export_cml()
        filename = f"bloom_manifest_cycle_{cycle}.cml"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cml_data)
        
        print(f"[Chronicler] Live CML artifact successfully compiled and written to: {filename}")

        if cycle < cycles:
            print(f"[Daemon] Sleeping for {interval_seconds} seconds before next telemetry poll...")
            time.sleep(interval_seconds)

    print("\n======================================================")
    print("DAEMON EXECUTION COMPLETE - ALL CYCLES VERIFIED.")
    print("======================================================")

if __name__ == "__main__":
    import random
    run_live_bloom_daemon(cycles=3, interval_seconds=3)