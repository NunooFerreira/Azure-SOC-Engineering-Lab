# Azure SOC Engineering Lab

This project demonstrates the end-to-end design and deployment of a **cloud-native Security Operations Center (SOC)** on **Microsoft Azure**.  
It includes the configuration of a honeypot virtual machine (VM), centralized log collection, SIEM integration with **Microsoft Sentinel**, log enrichment with geolocation data, and visualization of global attack sources through an interactive attack map.

The purpose of this lab is to simulate real-world SOC workflows — from telemetry ingestion and event analysis to visualization and threat detection — using modern cloud-native tools and security engineering principles.

---

## 🎯 Objectives

- Deploy a **Windows honeypot** VM in Azure to attract and capture malicious login attempts.
- Collect and centralize logs via **Log Analytics Workspace (LAW)**.
- Configure and enable **Microsoft Sentinel** as the SIEM for monitoring and correlation.
- Use **Azure Monitor Agent (AMA)** and **Data Collection Rules (DCR)** to forward Windows Security events.
- Enrich logs with **geolocation data** using Sentinel Watchlists.
- Visualize global attacker sources using a **Sentinel Workbook attack map**.
- Document the complete SOC engineering process, from setup to detection.

---

## 🧱 Architecture Overview


<img width="1411" height="660" alt="Diagrama sem nome drawio" src="https://github.com/user-attachments/assets/5fcc9fae-c007-4a27-b473-c88b3cdea825" />


---

## ⚙️ Components

| Component | Description |
|------------|-------------|
| **Azure VM (Windows Server)** | Honeypot machine that allows inbound RDP connections to simulate real-world attacks. |
| **Network Security Group (NSG)** | Configured to allow all inbound traffic for honeypot exposure. |
| **Azure Monitor Agent (AMA)** | Collects and forwards Windows Event Logs to the Log Analytics Workspace. |
| **Log Analytics Workspace (LAW)** | Centralized log storage and query engine. |
| **Microsoft Sentinel** | Cloud-native SIEM and SOAR used to analyze, detect, and visualize security events. |
| **GeoIP Watchlist** | Provides geolocation enrichment based on attacker IPs. |
| **Attack Map Workbook** | Interactive Sentinel dashboard showing global attack origins. |

---

## 🔍 Key KQL Queries

**1. View Failed Login Events (4625):**
```kql
SecurityEvent
| where EventID == 4625
| project TimeGenerated, Computer, Account = tostring(Account), IpAddress = tostring(IpAddress)
| order by TimeGenerated desc

let GeoIPDB_FULL = _GetWatchlist("geoip");
SecurityEvent
| where EventID == 4625
| where isnotempty(IpAddress)
| evaluate ipv4_lookup(GeoIPDB_FULL, IpAddress, network)
| summarize Count = count() by country_name, city_name, lat = todouble(lat), lon = todouble(lon)
| where isnotempty(lat) and isnotempty(lon)
| order by Count desc

