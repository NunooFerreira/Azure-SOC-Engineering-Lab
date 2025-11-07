# Successful Login After Multiple Failed Attempts (Microsoft Sentinel)

---

## Objective

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

## Analytics Rule Configuration

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

## Alert Showing Up in Microsoft Defender XDR:

<img width="1078" height="273" alt="image" src="https://github.com/user-attachments/assets/82a28ff6-0a9f-4d94-8467-8b571244545e" />

