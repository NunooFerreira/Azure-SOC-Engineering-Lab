# 🔎 Failed Login Threshold - Brute Force Detection (Microsoft Sentinel)

This section documents the configuration and behavior of the **Failed Login Threshold Rule**, designed to detect potential **brute-force attacks** on the Windows honeypot virtual machine deployed in the **Azure SOC Engineering Lab**.

---

## 🎯 Objective

The rule monitors **failed Windows logon attempts (Event ID 4625)** and triggers an **alert** when the same IP address generates **4 or more failed logins within a 10-minute window**.  
This pattern is typical of automated password-guessing or credential-stuffing attacks.

Once triggered, Microsoft Sentinel automatically creates an **incident**, allowing SOC analysts to investigate the source IP, attack frequency, and origin country.

---

## ⚙️ Analytics Rule Configuration

| Setting | Value |
|----------|--------|
| **Rule Name** | Failed Login Threshold - Brute Force |
| **Description** | Detects multiple failed logins from the same IP within a short time window. |
| **Severity** | Medium |
| **Status** | Enabled |
| **Query Frequency** | 5 minutes |
| **Query Period** | 10 minutes |
| **Trigger Threshold** | ≥ 4 failed logins per IP |
| **Event Grouping** | All events grouped into a single alert |
| **Incident Creation** | Enabled |

---

## 🧠 KQL Query

```kql
SecurityEvent
| where EventID == 4625
| where isnotempty(IpAddress)
| summarize FailCount = count() by IpAddress, bin(TimeGenerated, 10m)
| where FailCount >= 4
| extend DetectedTime = now(), AlertName = "FailedLoginThreshold"
| project DetectedTime, AlertName, IpAddress, FailCount
```
---
## Alert Showing Up:

<img width="1277" height="648" alt="BF_login" src="https://github.com/user-attachments/assets/7994b084-9452-4785-a3b7-76434b8b32c4" />


