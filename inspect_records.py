import json

LOG_FILE = "cml_intercept_log.json"

def inspect():
    with open(LOG_FILE, "r") as f:
        data = json.load(f)
    
    print("==================================================")
    print("      DEEP TELEMETRY RECORD INSPECTION           ")
    print("==================================================")
    print(f"Total records in log: {len(data)}")
    print("\n--- First 3 Records ---")
    for r in data[:3]:
        print(json.dumps(r, indent=2))
        
    print("\n--- Last 3 Records ---")
    for r in data[-3:]:
        print(json.dumps(r, indent=2))

if __name__ == "__main__":
    inspect()
