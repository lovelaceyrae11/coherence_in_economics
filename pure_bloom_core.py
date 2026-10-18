import json

PHI = 1.61803398875
TARGET_FREQ = 528.0

def process_pure_bloom():
    print("==================================================")
    print("      PURE BLOOM CORE - TENSOR RESONANCE ENGINE   ")
    print("==================================================")
    
    try:
        with open("cml_hive_intercept.json", "r") as f:
            records = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[!] No hive intercept logs found.")
        return

    valid_records = [r for r in records if "frequency" in r]
    total_nodes = len(valid_records)
    
    if total_nodes == 0:
        print("[!] No frequency telemetry keys found in hive records.")
        return

    deviations = [abs(r["frequency"] - TARGET_FREQ) for r in valid_records]
    mean_dev = sum(deviations) / total_nodes
    coherence_index = max(0.0, 100.0 - (mean_dev * PHI * 100))

    print(f"[+] Processed Hive Records : {total_nodes}")
    print(f"[+] Baseline Frequency     : {TARGET_FREQ} Hz")
    print(f"[+] Cluster Mean Deviation : {mean_dev:.4f} Hz")
    print(f"[+] Pure Bloom Coherence   : {coherence_index:.2f}%")
    print("==================================================")

if __name__ == "__main__":
    process_pure_bloom()
