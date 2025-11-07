# 🔐 Successful Login After Multiple Failed Attempts (Microsoft Sentinel)

This section documents the configuration and behavior of the **Successful Login After Multiple Failed Attempts** rule, developed to detect potential **credential compromise** on the Windows honeypot virtual machine deployed within the **Azure SOC Engineering Lab**.

---

## 🎯 Objective

This rule identifies scenarios where a **successful Windows logon (Event ID 4624)** occurs **shortly after multiple failed attempts (Event ID 4625)** from the **same IP address**.

Such a pattern often indicates:
- A brute-force or credential-stuffing attack that has finally succeeded  
- Unauthorized access attempts from an external host  
- A compromised account being accessed by an attacker after repeated trial-and-error login attempts  

When triggered, **Microsoft Sentinel** automatically generates an **incident**, allowing SOC analysts to:
- Review the IP address involved  
- Verify if the user account or device is legitimate  
- Correlate with threat intelligence or lateral movement activity  

---

## ⚙️ Analytics Rule Configuration

| Setting | Value |
|----------|--------|
| **Rule Name** | Successful Login After Multiple Failed Attempts |
| **Description** | Detects a successful login (4624) from an IP that previously failed multiple logins (4625) within a short time window. |
| **Tactics** | Credential Access, Persistence |
| **Severity** | Medium |
| **Status** | Enabled |
| **Query Frequency** | 10 minutes |
| **Query Period** | 30 minutes |
| **Trigger Threshold** | ≥ 1 correlated event |
| **Event Grouping** | All correlated events grouped into a single alert |
| **Incident Creation** | Enabled |

---

## 🧠 KQL Query

```kql
let fails = SecurityEvent
| where TimeGenerated >= ago(30m)
| where EventID == 4625
| where isnotempty(IpAddress)
| summarize FailCount = count(), LastFail = max(TimeGenerated) by IpAddress;
let successes = SecurityEvent
| where TimeGenerated >= ago(30m)
| where EventID == 4624
| where isnotempty(IpAddress)
| project SuccessTime = TimeGenerated, IpAddress, Account;
successes
| join kind=inner (fails) on IpAddress
| where SuccessTime >= LastFail and SuccessTime <= datetime_add('minute', 30, LastFail)
| extend DetectedTime = now(), AlertName = "SuccessAfterFailures", FailedAttempts = FailCount
| project DetectedTime, AlertName, IpAddress, Account, FailedAttempts, LastFail, SuccessTime
| sort by DetectedTime desc
