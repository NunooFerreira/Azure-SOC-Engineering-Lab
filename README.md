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

## 📊 Project Workflow

1. **Deploy Azure VM** – Create and expose a Windows honeypot instance.  
2. **Generate Events** – Attempt RDP logins (Event ID 4625) to produce failed login logs.  
3. **Forward Logs** – Use Azure Monitor Agent (AMA) and Data Collection Rules (DCR) to send logs to LAW.  
4. **Connect Sentinel** – Enable Microsoft Sentinel on the workspace for SIEM capabilities.  
5. **Enrich Data** – Add GeoIP Watchlist for attacker location mapping.  
6. **Visualize Attacks** – Build Sentinel Workbook (Attack Map) to show global attack traffic.  

---

## 📁 Project Structure

azure-soc-engineering-lab/
│
├── /docs
│ ├── 01-azure-setup.md
│ ├── 02-honeypot-vm.md
│ ├── 03-log-analytics-workspace.md
│ ├── 04-sentinel-setup.md
│ ├── 05-log-forwarding.md
│ ├── 06-log-enrichment.md
│ ├── 07-attack-map-workbook.md
│ └── 08-results-and-analysis.md
│
├── /assets
│ ├── architecture-diagram.png
│ ├── attack-map-screenshot.png
│ └── event-4625-example.png
│
└── README.md



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

