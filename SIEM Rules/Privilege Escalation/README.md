# Privilege Escalation — User Added to Administrators Group (Microsoft Sentinel)

This section documents the configuration and behaviour of the **Privilege Escalation** detection rule that alerts when a user account is added to an **Administrators** (privileged) group on the Windows honeypot VM in the **Azure SOC Engineering Lab**.

---

## Objective

Detect when an account is added to a privileged/local **Administrators** group (common indicator of privilege escalation).  
This helps the SOC identify when an attacker tries to gain persistence or escalate privileges after initial access.

---

## Analytics Rule Configuration

| Setting | Value |
|---|---|
| **Rule Name** | Privilege Escalation — User Added to Administrators Group |
| **Description** | Detects group membership additions where the target group is a privileged Administrators group (EventIDs: 4728, 4732, 4756, 4727). |
| **Severity** | High |
| **Status** | Enabled |
| **Query Frequency** | 1 hour |
| **Query Period** | 24 hours |
| **Trigger Threshold** | ≥ 1 matching event |
| **Event Grouping** | Group alerts by `AddedMember` or `GroupName` into a single alert |
| **Incident Creation** | Enabled |
| **Suppression** | 6 hours (per `AddedMember`) — recommended to avoid alert storms on repeated legitimate changes |

---
