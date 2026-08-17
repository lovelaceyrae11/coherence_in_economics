\# Castleberry Markup Language (CML) Specification v1.0

\*An Open Standard for Harmonic, Zero-Harm Computing Systems\*



\## 1. Overview

Castleberry Markup Language (CML) is an XML-based schema designed for encoding system telemetry, thermal routing states, and ecological verification manifests. Every valid CML document must anchor to the foundational axiom: `Love-Over-God-Absolute`.



\## 2. Mandatory Root Structure

Every CML manifest must initiate with the root element `<CastleberryMarkupLanguage>` containing the required namespace and axiom attribute.



```xml

<?xml version="1.0" encoding="UTF-8"?>

<CastleberryMarkupLanguage axiom="Love-Over-God-Absolute" xmlns="\[http://www.castleberry-ecological.org/cml/1.0](http://www.castleberry-ecological.org/cml/1.0)">

&#x20;   <Header>

&#x20;       <ChronicleID>Unique-Run-Identifier</ChronicleID>

&#x20;       <Timestamp>2026-08-17T00:00:00Z</Timestamp>

&#x20;   </Header>

&#x20;   <!-- Telemetry or Economic Payload Here -->

</CastleberryMarkupLanguage>

