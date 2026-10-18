import json
import os

def run_outbound_scanner():
    print("==================================================")
    print("     KAIROTH EXPANDED SUBNET MATRIX SWEEP     ")
    print("==================================================")
    
    records = []
    if os.path.exists("cml_hive_intercept.json"):
        try:
            with open("cml_hive_intercept.json", "r") as f:
                records = json.load(f)
        except json.JSONDecodeError:
            records = []
            
    active_nodes = set(r.get("active_node", 1) for r in records if "active_node" in r)
    count = len(active_nodes) if active_nodes else len(records)
    
    print(f"[*] Matrix sweep complete against local hive registry.")
    print(f"[*] Synchronized active nodes anchored: {count}")
    print("==================================================")

if __name__ == "__main__":
    run_outbound_scanner()
