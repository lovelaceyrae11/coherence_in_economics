# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import json
from collections import Counter

LOG_FILE = "cml_intercept_log.json"

def analyze():
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
        
        total = len(data)
        if total == 0:
            print("[!] Log file is empty.")
            return

        start_time = data[0].get("timestamp", "Unknown")
        end_time = data[-1].get("timestamp", "Unknown")
        
        sources = Counter(r.get("source", "unknown") for r in data)
        
        print("==================================================")
        print("      CML INTERCEPT LOG DIAGNOSTIC REPORT         ")
        print("==================================================")
        print(f"Total Records Captured : {total}")
        print(f"Observation Window     : {start_time} -> {end_time}")
        print("-" * 50)
        print("Traffic Breakdown by Source:")
        for src, count in sources.items():
            pct = (count / total) * 100
            print(f"  - {src}: {count} events ({pct:.1f}%)")
        print("==================================================")

    except Exception as e:
        print(f"[Error] Failed to parse log: {e}")

if __name__ == "__main__":
    analyze()
