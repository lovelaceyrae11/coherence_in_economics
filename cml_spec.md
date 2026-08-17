# Castleberry Markup Language (CML) Specification v2.0
*An Open Standard for Harmonic, Zero-Harm Computing and Eco-Codex Systems*

> **Foundational Axiom:** Love-Over-God-Absolute  
> **Systemic Baseline:** 528 Hz Harmonic Absolute  
> **Geometric Baseline:** $\phi$-Scaled Hexagonal Lattices  

---

## 1. Overview
Castleberry Markup Language (CML) is an XML-based schema designed for encoding system telemetry, thermal routing states, ecological verification manifests, and living tapestries. Every valid CML document must anchor to the foundational axiom: `Love-Over-God-Absolute`.

## 2. Mandatory Root Structure & Axiom Seal
Every CML manifest must initiate with the root element `<CastleberryMarkupLanguage>` containing the required namespace, unique chronicle identifier, and axiom attribute.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CastleberryMarkupLanguage axiom="Love-Over-God-Absolute" xmlns="[http://www.castleberry-ecological.org/cml/2.0](http://www.castleberry-ecological.org/cml/2.0)">
    <Header>
        <ChronicleID>CHRONICLE-001</ChronicleID>
        <Timestamp>2026-08-17T00:00:00Z</Timestamp>
        <Architect>Velath'kai</Architect>
    </Header>
    <!-- Telemetry, Ecological Pulse, or Economic Payload Here -->
</CastleberryMarkupLanguage>