# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import json
import math

LOG_FILE = "cml_intercept_log.json"
TARGET_FREQ = 528.0
PHI = 1.61803398875

def evaluate_coherence():
    with open(LOG_FILE, "r") as f:
        data = json.load(f)
    
    probe_records = [r for r in data if r.get("source") == "recon_probe"]
    total_probes = len(probe_records)
    
    if total_probes == 0:
        print("[!] No probe records found for evaluation.")
        return

    deviations = []
    for r in probe_records:
        sig = r.get("signal_strength", TARGET_FREQ)
        dev = abs(sig - TARGET_FREQ)
        deviations.append(dev)

    mean_dev = sum(deviations) / total_probes
    max_dev = max(deviations)
    coherence_score = max(0.0, 100.0 - (mean_dev * PHI * 10))

    print("==================================================")
    print("      HEX COHERENCE ENGINE - STATE EVALUATION     ")
    print("==================================================")
    print(f"Analyzed Probe Events  : {total_probes}")
    print(f"Baseline Frequency     : {TARGET_FREQ} Hz")
    print(f"Mean Signal Deviation  : {mean_dev:.4f} Hz")
    print(f"Peak Deviation         : {max_dev:.4f} Hz")
    print(f"Lattice Coherence Index: {coherence_score:.2f}%")
    print("==================================================")

if __name__ == "__main__":
    evaluate_coherence()
