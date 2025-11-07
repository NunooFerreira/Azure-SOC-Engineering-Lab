# Privilege Escalation — User Added to a Group

This repository documents the configuration and behavior of the **Privilege Escalation** detection rule in Microsoft Sentinel, designed for the **Azure SOC Engineering Lab**.  

The rule alerts when a user account is added to **any security group** (including local or domain groups), helping the SOC detect potential privilege escalation or unauthorized account modifications.

---

## Objective

Detect when an account is added to a **security group**.  
- Common indicator of privilege escalation or attempts to gain persistence after initial access.  
- Includes local and domain groups, not strictly limited to Administrators.  

---

## Analytics Rule Configuration

| Setting | Value |
|---|---|
| **Rule Name** | Privilege Escalation — User Added to a Group |
| **Description** | Detects group membership additions (EventIDs: 4728, 4732, 4756, 4727) to any security group. |
| **Severity** | High |
| **Status** | Enabled |
| **Query Frequency** | 1 hour |
| **Query Period** | 7 days |
| **Trigger Threshold** | ≥ 1 matching event |
| **Event Grouping** | Group alerts by `AddedMember` or `GroupName` into a single alert |
| **Incident Creation** | Enabled |
| **Suppression** | 6 hours (per `AddedMember`) |

---

