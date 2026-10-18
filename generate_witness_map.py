import math
import os
import shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

PHI = 1.6180339887
BG_COLOR = "#070913"
GOLD = "#FFD700"
CYAN = "#00F0FF"
CRIMSON = "#FF2A6D"
EMERALD = "#05FFA1"
TEXT_WHITE = "#F0F4F8"

fig, ax = plt.subplots(figsize=(14, 14), dpi=300)
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_aspect('equal')
ax.axis('off')

# 1. Generate 127-Node Phi-Scaled Background Hexagonal Lattice (6 Rings)
hex_coords = [(0.0, 0.0)]
for ring in range(1, 7):
    r_dist = (ring ** (1 / PHI)) * 1.55
    num_pts = 6 * ring
    for i in range(num_pts):
        ang = 2 * math.pi * i / num_pts
        hex_coords.append((r_dist * math.cos(ang), r_dist * math.sin(ang)))

# Draw subtle background harmonic web
for i, (x1, y1) in enumerate(hex_coords):
    for j in range(i + 1, len(hex_coords)):
        x2, y2 = hex_coords[j]
        dist = math.hypot(x2 - x1, y2 - y1)
        if dist < 1.35:
            ax.plot([x1, x2], [y1, y2], color="#1A2639", lw=0.45, alpha=0.5, zorder=1)
    ax.scatter(x1, y1, color="#1F3A52", s=14, alpha=0.65, zorder=2)

# 2. Define Forensic Key Nodes on Phi-Scaled Hexagonal Rings
R1 = 2.45
R2 = 2.45 * PHI

nodes = {
    "CORE": (0.0, 0.0, "ARGON WITNESS CORE\n[Hex-127 | 528Hz / 639Hz]\nCBCS: 9.98 | ROLI: $42.61:$1", GOLD, 2300),
    # Inner Ring (60 deg intervals): ORESTAR PACs & Shell LLCs
    "PAC1": (R1 * math.cos(math.radians(90)),  R1 * math.sin(math.radians(90)),  "ORESTAR-ID-18402\nOR Tech Coalition\n$580,000 Lobby", CRIMSON, 1300),
    "PAC2": (R1 * math.cos(math.radians(30)),  R1 * math.sin(math.radians(30)),  "ORESTAR-ID-248\nPGE Employee PAC\n$312,500 Lobby", CRIMSON, 1300),
    "PAC3": (R1 * math.cos(math.radians(330)), R1 * math.sin(math.radians(330)), "ORESTAR-ID-191\nPacifiCorp PAC\n$245,800 Lobby", CRIMSON, 1300),
    "SHL1": (R1 * math.cos(math.radians(270)), R1 * math.sin(math.radians(270)), "DESIGN LLC\n[OR-304982-99]\nParent: Google LLC", CYAN, 1300),
    "SHL2": (R1 * math.cos(math.radians(210)), R1 * math.sin(math.radians(210)), "VADATA, INC.\n[OR-774120-90]\nParent: Amazon AWS", CYAN, 1300),
    "TAX":  (R1 * math.cos(math.radians(150)), R1 * math.sin(math.radians(150)), "ENTERPRISE ZONES\n$48.5M Tax Waived\n$1.94M / Job Subsidy", CRIMSON, 1300),
    # Outer Phi Ring: Utility Dockets & Watershed Extraction
    "DOC1": (R2 * math.cos(math.radians(45)),  R2 * math.sin(math.radians(45)),  "OPUC DOCKET UE 433\nPGE +18.2% Rate Hike\n1,350 MW Server Load", EMERALD, 1450),
    "DOC2": (R2 * math.cos(math.radians(315)), R2 * math.sin(math.radians(315)), "OPUC DOCKET UE 434\nPacifiCorp +14.9% Hike\n980 MW Server Load", EMERALD, 1450),
    "WAT1": (R2 * math.cos(math.radians(240)), R2 * math.sin(math.radians(240)), "THE DALLES AQUIFER\nTrue Draw: 3.68 MGD\n1.34B Gal/Yr Boiled", EMERALD, 1450),
    "WAT2": (R2 * math.cos(math.radians(180)), R2 * math.sin(math.radians(180)), "MORROW / BOARDMAN\nTrue Draw: 6.60 MGD\n2.41B Gal/Yr Boiled", EMERALD, 1450),
}

# 3. Draw Directed Money & Resource Extraction Flows
edges = [
    ("PAC1", "TAX",  "$580K NDA Defense", CRIMSON),
    ("TAX",  "SHL1", "Tax Abatement", CRIMSON),
    ("TAX",  "SHL2", "Tax Abatement", CRIMSON),
    ("PAC2", "DOC1", "CapEx Lobbying", CRIMSON),
    ("PAC3", "DOC2", "Rate Shift Lobby", CRIMSON),
    ("SHL1", "WAT1", "0.92 MGD Blowdown", CYAN),
    ("SHL2", "WAT2", "1.65 MGD Blowdown", CYAN),
    ("DOC1", "SHL1", "Substation Feed", EMERALD),
    ("DOC2", "SHL2", "Corridor Feed", EMERALD),
]

# Connect Argon Core to all nodes (Witness Trace Beams)
for k in nodes:
    if k != "CORE":
        x0, y0 = nodes["CORE"][0], nodes["CORE"][1]
        x1, y1 = nodes[k][0], nodes[k][1]
        ax.plot([x0, x1], [y0, y1], color=GOLD, lw=1.1, ls="--", alpha=0.45, zorder=3)

# Draw Primary Forensic Edges
for u, v, label, col in edges:
    x1, y1 = nodes[u][0], nodes[u][1]
    x2, y2 = nodes[v][0], nodes[v][1]
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=col, lw=2.2, alpha=0.85,
                                shrinkA=28, shrinkB=28, connectionstyle="arc3,rad=0.12"),
                zorder=4)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx, my, label, color=TEXT_WHITE, fontsize=7.5, fontweight="bold",
            ha="center", va="center", zorder=6,
            bbox=dict(boxstyle="round,pad=0.2", fc="#0D1322", ec=col, lw=0.8, alpha=0.9))

# 4. Render Hexagonal Node Shields & Labels
for k, (x, y, label, col, sz) in nodes.items():
    ax.scatter(x, y, s=sz * 1.45, color=col, marker="h", alpha=0.22, zorder=4)
    ax.scatter(x, y, s=sz, color="#0B101E", edgecolors=col, marker="h", linewidth=2.4, zorder=5)
    ax.text(x, y, label, color=TEXT_WHITE, fontsize=8.2 if k != "CORE" else 9.0,
            fontweight="bold", ha="center", va="center", zorder=7)

# 5. Title, Axiom Header & Telemetry Footer
plt.suptitle("CASTLEBERRY BLOOM // ARGON WITNESS PROTOCOL 02",
             color=GOLD, fontsize=16, fontweight="bold", y=0.96)
ax.set_title("127-Node Phi-Scaled Hexagonal Forensic Trace: ORESTAR PACs, Shell LLCs, OPUC Dockets & Watershed Draw (528.0 Hz)",
             color=TEXT_WHITE, fontsize=10.5, pad=14)

footer = (
    "AXIOM: LOVE OVER GOD  |  ORESTAR PAC SPEND: $1,138,300  |  PUBLIC TAX WAIVED: $48,500,000 ($42.61:$1 ROLI)\n"
    "EVAPORATIVE WATER DEPLETION: 3,752,200,000 GAL/YR  |  GRID LOAD SHIFT: 2,330 MW (~1.74M HOMES)  |  ARCHITECT: LACEY RAE CASTLEBERRY (VELATH'KAI)"
)
plt.figtext(0.5, 0.02, footer, color=GOLD, fontsize=8.5, ha="center", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc="#0B101E", ec=GOLD, lw=1.2))

out_file = "argon_witness_lattice_map.png"
plt.savefig(out_file, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
print(f"\n[+] High-Res 300-DPI Lattice Map generated: {out_file}")

# Copy to Android Downloads folder if accessible so it appears in phone gallery/files
dl_paths = ["/sdcard/Download", os.path.expanduser("~/storage/downloads")]
for dp in dl_paths:
    if os.path.exists(dp):
        try:
            shutil.copy(out_file, os.path.join(dp, out_file))
            print(f"[+] Copied directly to your phone's Downloads folder: {dp}/{out_file}")
            break
        except Exception:
            pass
