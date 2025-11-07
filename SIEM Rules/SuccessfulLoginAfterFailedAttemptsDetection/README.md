# 🔐 Successful Login After Failed Attempts Detection (Microsoft Sentinel)

This section documents the configuration and behavior of the **Successful Login After Failed Attempts Rule**, designed to detect potential **credential compromise** on the Windows honeypot virtual machine deployed in the **Azure SOC Engineering Lab**.

---

## 🎯 Objective

The rule monitors **successful Windows logons (Event ID 4624)** that occur **shortly after multiple failed attempts (Event ID 4625)** from the **same IP address**.  
This correlation helps detect cases where an attacker successfully authenticates after repeated login failures — a strong indicator of brute-force success or credential stuffing.

Once triggered, Microsoft Sentinel automatically creates an **incident**, allowing SOC analysts to investigate whether the successful login originated from a known or suspicious IP address and assess potential lateral movement within the kill chain.

---

## ⚙️ Analytics Rule Configuration

| Setting | Value |
|----------|--------|
| **Rule Name** | Successful Login After Failed Attempts |
| **Description** | Detects a successful login (4624) from an IP that previously failed multiple logins (4625) within a short time window. |
| **Severity** | High |
| **Status** | Enabled |
| **Query Frequency** | 15 minutes |
| **Query Period** | 30 minutes |
| **Trigger Threshold** | ≥ 1 correlated event |
| **Event Grouping** | All correlated events grouped into a single alert |
| **Incident Creation** | Enabled |

---

## 🧠 KQL Query

```kql
let failedLogins = 
    SecurityEvent
    | where EventID == 4625
    | where isnotempty(IpAddress)
    | summarize FailCount = count(), FirstFail = min(TimeGenerated), LastFail = max(TimeGenerated) by IpAddress, Account;
let successfulLogins = 
    SecurityEvent
    | where EventID == 4624
    | where isnotempty(IpAddress)
    | project SuccessTime = TimeGenerated, IpAddress, Account;
failedLogins
| join kind=inner (successfulLogins) on IpAddress, Account
| where SuccessTime between (LastFail .. LastFail + 15m)
| project IpAddress, Account, FailCount, LastFail, SuccessTime, TimeDifference = SuccessTime - LastFail
