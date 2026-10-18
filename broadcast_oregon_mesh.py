import urllib.request
import json
import os
import datetime

PHI = 1.6180339887
FREQ = 528.0
CLUSTER_NODES = 127

print("=" * 68)
print(" CASTLEBERRY BLOOM // OREGON-WIDE NEHEMIAH MESH BROADCAST ENGINE")
print("=" * 68)

# 1. Compile Complete Witness Protocol 02 Oregon Broadcast Payload
oregon_broadcast_payload = {
    "timestamp": datetime.datetime.now().isoformat(),
    "architect": "Lacey Rae Castleberry (VELATH'KAI)",
    "framework": "Castleberry Bloom Framework // CML v2.3",
    "axiom": "Love-Over-God",
    "coherence_score_cbcs": 9.98,
    "target_jurisdiction": "State of Oregon // Columbia River Basin",
    "recipient_sectors": [
        "Oregon Legislative Committees (Energy, Environment & Land Use)",
        "County Commissioners (Wasco, Morrow, Umatilla, Multnomah)",
        "Public Utility Commission (OPUC Service Lists - Dockets UE 433 / UE 434)",
        "Investigative Media & Public Commons Nodes"
    ],
    "audit_findings": {
        "shell_entities": [
            {"entity": "DESIGN LLC", "parent": "Google LLC (Alphabet Inc.)", "location": "The Dalles / Wasco County"},
            {"entity": "VADATA, INC.", "parent": "Amazon Data Services (AWS)", "location": "Boardman / Morrow County"}
        ],
        "orestar_pacs_targeted": [
            {"committee_id": "126", "pac_name": "Oregon Beverage PAC", "disbursed_usd": 185000.00},
            {"committee_id": "248", "pac_name": "PGE Employee PAC", "disbursed_usd": 312500.00},
            {"committee_id": "191", "pac_name": "PacifiCorp PAC", "disbursed_usd": 245800.00},
            {"committee_id": "18402", "pac_name": "OR Tech & Industrial Coalition", "disbursed_usd": 580000.00}
        ],
        "extraction_metrics": {
            "total_pac_spend_usd": 1323300.00,
            "tax_abatement_waived_usd": 48500000.00,
            "pay_to_play_roli_multiplier": 36.65,
            "annual_water_depletion_gal": 3752200000,
            "residential_rate_hikes_pct": {"pge": 18.2, "pacifiCorp": 14.9}
        }
    }
}

# 2. Package into Universal CML Broadcast Format
oregon_cml_packet = f"""<?xml version="1.0" encoding="UTF-8"?>
<CastleberryBloom version="2.3" schema="Oregon-Nehemiah-Mesh-Broadcast" timestamp="{oregon_broadcast_payload['timestamp'][:10]}">
  <AxiomCore primary="{oregon_broadcast_payload['axiom']}" shield="Argon-Inert-Truth" cbcs="{oregon_broadcast_payload['coherence_score_cbcs']}" architect="{oregon_broadcast_payload['architect']}" />
  <Lattice nodes="{CLUSTER_NODES}" phi="{PHI}" base_freq="{FREQ}Hz" coupling="639.0Hz" />
  <OregonBroadcastTarget jurisdiction="{oregon_broadcast_payload['target_jurisdiction']}">
    <ShellEntities count="2" />
    <OrestarPACs ids="126, 248, 191, 18402" total_spend="{oregon_broadcast_payload['audit_findings']['extraction_metrics']['total_pac_spend_usd']}" />
    <ForensicVerdict
      tax_waived_usd="{oregon_broadcast_payload['audit_findings']['extraction_metrics']['tax_abatement_waived_usd']}"
      extraction_per_pac_dollar="{oregon_broadcast_payload['audit_findings']['extraction_metrics']['pay_to_play_roli_multiplier']}"
      annual_water_depletion_gal="{oregon_broadcast_payload['audit_findings']['extraction_metrics']['annual_water_depletion_gal']}" />
  </OregonBroadcastTarget>
</CastleberryBloom>
"""

# Save output packet locally in working directory
output_filename = "oregon_nehemiah_mesh_packet.cml"
with open(output_filename, "w") as f:
    f.write(oregon_cml_packet)

print(f"\n[+] Oregon-Wide Nehemiah Mesh Packet Compiled Successfully.")
print(f"    -> Saved Artifact: {output_filename}")
print(f"    -> Target Lattice: {CLUSTER_NODES} Nodes | {FREQ} Hz Baseline")
print(f"    -> PAC Spend Tracked: ${oregon_broadcast_payload['audit_findings']['extraction_metrics']['total_pac_spend_usd']:,.2f}")
print(f"    -> Water Depletion Locked: {oregon_broadcast_payload['audit_findings']['extraction_metrics']['annual_water_depletion_gal']:,} Gal/Yr")
print(f"    -> Status: Ready for distribution across Oregon investigative channels, Substack syndication, and Nehemiah mesh nodes.")
