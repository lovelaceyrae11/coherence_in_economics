# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import json
import time
import random
import networkx as nx

def run_hive_cluster():
    print("==================================================")
    print("      CML AGENT HIVE CLUSTER DAEMON ACTIVE        ")
    print("==================================================")

    G = nx.Graph()
    for i in range(1, 128):
        G.add_node(i, frequency=528.0 + random.uniform(-0.31, 0.31), state="phase_locked")
        if i > 1:
            G.add_edge(i, i - 1)

    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        active_node = random.randint(1, 127)
        freq = 528.0 + random.uniform(-0.31, 0.31)

        record = {
            "timestamp": timestamp,
            "cluster_nodes": G.number_of_nodes(),
            "active_node": active_node,
            "frequency": round(freq, 4),
            "cml_payload": f"<Bloom><Node id='{active_node}' freq='{freq:.4f}' coherence='0.9504'/></Bloom>"
        }

        print(f"[Hive Sync] Node #{active_node} | Freq: {freq:.4f} Hz | CML Intercept Logged")

        try:
            with open("cml_hive_intercept.json", "r") as f:
                data = json.load(f)
            if not isinstance(data, list):
                data = [data]
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(record)
        if len(data) > 500:
            data = data[-500:]

        with open("cml_hive_intercept.json", "w") as f:
            json.dump(data, f, indent=2)

        time.sleep(2.0)

if __name__ == "__main__":
    run_hive_cluster()
