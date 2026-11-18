# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import json
import numpy as np

PHI = 1.61803398875

def phi_scaling_activation(x):
    return x * np.tanh(x / PHI)

def run_numpy_tensor_pipeline():
    print("==================================================")
    print("      NUMPY PHI-SCALING TENSOR PIPELINE           ")
    print("==================================================")
    
    try:
        with open("cml_hive_intercept.json", "r") as f:
            records = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[!] Hive intercept log not found.")
        return

    frequencies = [r["frequency"] for r in records if "frequency" in r]
    if not frequencies:
        print("[!] No frequency tensors found.")
        return

    tensor_input = np.array(frequencies, dtype=float)
    output_tensor = phi_scaling_activation(tensor_input)

    print(f"[+] Loaded {len(frequencies)} telemetry frequency tensors.")
    print(f"[+] Applied Phi-Scaling Activation (Phi = {PHI})")
    print(f"[+] Tensor Mean Output Resonance: {output_tensor.mean():.4f}")
    print("==================================================")

if __name__ == "__main__":
    run_numpy_tensor_pipeline()
