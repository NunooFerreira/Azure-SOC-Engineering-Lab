# Automation

This directory contains lightweight automation utilities developed to validate log ingestion, detect parsing issues, and ensure the health of the Azure SOC pipeline.  
These scripts replicate tasks such as onboarding checks, parser validation, and ingestion monitoring.

---

##  Overview

As part of the **Azure SOC Engineering Lab**, three automation scripts were created to improve **visibility**, **diagnostics**, and **reliability** across the telemetry pipeline:

-  Onboarding validation of a new log source  
-  Parsing verification before logs reach Sentinel  
-  Continuous agent health and ingestion delay monitoring  

These tools mimic real-world SIEM operational workflows used by SOC engineering teams.

---

#  Script 1 — AMA Status & Heartbeat Check (check_siem_health.sh)

###  Purpose
Provides a quick verification of the Azure Monitor Agent (AMA) health by checking whether the service is running, confirming recent heartbeat activity, and reviewing the latest system log events.


###  What It Checks
- AMA service status: Verifies whether azuremonitoragent is active and running correctly. 
- Recent heartbeat logs  
- Heartbeat logs: Searches recent system logs for AMA heartbeat events, which indicate that the agent is alive and communicating.
- Last 10 syslog events: Displays the most recent syslog entries for additional context or troubleshooting.

###  Why It's Useful
This script acts as a fast diagnostic tool during onboarding or troubleshooting, helping determine whether AMA is operational and actively generating heartbeats. It is a lightweight first step before deeper ingestion or DCR checks.

### Example Output
<img width="886" height="303" alt="image" src="https://github.com/user-attachments/assets/5c20bd82-c7f3-43cf-8a2f-3855de89efbb" />

---

# Script 2 — Last Syslog Timestamp Viewer (last_log_check.sh)

###  Purpose
Retrieves and displays the timestamp of the most recent syslog entry.
 

 Large delays (e.g., > 5 minutes) may indicate:

### What It Does
- Reads the last line of /var/log/syslog
- Extracts only the timestamp portion (e.g., Jan 12 14:03:21)
- Prints it for quick inspection

### Why It's Useful
This script provides a simple way to confirm that syslog is actively writing new entries.
It is especially useful during troubleshooting steps where you need to verify that logs are still being generated on the system.

### Example Output
<img width="613" height="38" alt="image" src="https://github.com/user-attachments/assets/253c8586-4125-4aff-8b57-475dfd00ce64" />

---

#  Script 3 — Syslog Parsing Validation (`parser_test.py`)

###  Purpose
Validates how logs are parsed before entering Sentinel.  
Simulates a SIEM parser by normalizing the raw syslog record.

###  What It Does

1. Reads the last log line from:

2. Extracts fields:
- Timestamp  
- Hostname  
- Process  
- Message  
3. Detects optional values:
- User  
- IP address  
4. Creates a **SIEM-style normalized JSON object**  
5. Flags unexpected log formats  

###  Why It's Useful
Even small parsing problems affect:

- Analytics rule matching  
- Field extraction  
- Alert quality  
- Event correlation  

This script helps catch parsing issues early.

### Example Output

<img width="696" height="495" alt="image" src="https://github.com/user-attachments/assets/5aca8ebe-9401-4a1b-b7d5-7e9ff44a3be5" />

