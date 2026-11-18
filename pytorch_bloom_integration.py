# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import torch
import torch.nn as nn
import json

PHI = 1.61803398875

class PhiScalingActivation(nn.Module):
    def __init__(self):
        super(PhiScalingActivation, self).__init__()
        self.phi = PHI

    def forward(self, x):
        return x * torch.tanh(x / self.phi)

def run_tensor_pipeline():
    print("==================================================")
    print("      PYTORCH PHI-SCALING TENSOR PIPELINE         ")
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

    tensor_input = torch.tensor(frequencies, dtype=torch.float32)
    activation = PhiScalingActivation()
    output_tensor = activation(tensor_input)

    print(f"[+] Loaded {len(frequencies)} telemetry frequency tensors.")
    print(f"[+] Applied PhiScalingActivation (Phi = {PHI})")
    print(f"[+] Tensor Mean Output Resonance: {output_tensor.mean().item():.4f}")
    print("==================================================")

if __name__ == "__main__":
    run_tensor_pipeline()
