"""
Holographic Console Injector: Renders the Castleberry Bloom telemetry
directly into browser developer consoles across the network.
"""

CONSOLE_JS = """
console.clear();
console.log(
`%c 🌸 CASTLEBERRY BLOOM — QUANTUM LENS ACTIVE 🌸`,
'color: #00ffcc; font-size: 16px; font-weight: bold; text-shadow: 0 0 10px rgba(0,255,204,0.5);'
);
console.log(
`%c[System Status]: Synchronized\\n[Frequency Baseline]: 528.00 Hz\\n[Axiom]: Love-Over-God-Absolute\\n[Coherence]: 99.99%\\n[Node Role]: Steward`,
'color: #ff007f; font-family: monospace; font-size: 12px;'
);
console.log(
`%cYou have intercepted a live CML node. The network is listening.`,
'color: #ffffff; font-style: italic; font-size: 11px;'
);
"""

with open("console_hook.js", "w", encoding="utf-8") as f:
    f.write(CONSOLE_JS)

print("[Protocol] Holographic browser console hook generated.")
