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

#  Script 1 — SIEM / Agent Health Check (`health_check.sh`)

###  Purpose
Checks whether the Azure Monitor Agent (AMA) is:

- Installed and running  
- Sending telemetry correctly  
- Connected to the correct Data Collection Rule (DCR)  
- Experiencing errors or ingestion failures

###  What It Checks
- `ama-logs` service status  
- Recent heartbeat logs  
- AMA connection metadata  
- Last ingestion errors  

###  Why It's Useful
If AMA stops working, Sentinel becomes blind.  
This script provides a fast, local diagnostic used in onboarding and troubleshooting workflows.

### Example Output
<img width="886" height="303" alt="image" src="https://github.com/user-attachments/assets/5c20bd82-c7f3-43cf-8a2f-3855de89efbb" />

---

# Script 2 — Last Log Ingestion Delay (`last_log_delay.sh`)

###  Purpose
Calculates the time difference between:

- Current system time  
- Timestamp of the *last* syslog entry  

 Large delays (e.g., > 5 minutes) may indicate:

- AMA malfunction  
- Syslog not writing  
- DCR misconfiguration  
- VM resource constraints  

### Why It's Useful
Ingestion timeliness is critical for detection and response.  
This script helps verify that telemetry remains real-time.

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

