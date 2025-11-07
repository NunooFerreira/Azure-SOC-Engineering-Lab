# Failed Login Threshold - Brute Force Detection

---

## Objective

The rule monitors **failed Windows logon attempts (Event ID 4625)** and triggers an **alert** when the same IP address generates **4 or more failed logins within a 10-minute window**.  
This pattern is typical of automated password-guessing or credential-stuffing attacks.

Once triggered, Microsoft Sentinel automatically creates an **incident**, allowing SOC analysts to investigate the source IP, attack frequency, and origin country.

---

## Analytics Rule Configuration

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
## 📩 Email Automation

Created a Logic App playbook.

When an incident is created (Microsoft Sentinel Incident V3).

Action: Send email via Office 365 Outlook (Send an email V2) connector.

Connected the playbook to the rule through a Sentinel Automation Rule, ensuring an email alert is sent automatically each time the analytic rule generates an incident.

---
## Alert Showing Up in Microsoft Defender XDR:

<img width="674" height="159" alt="image" src="https://github.com/user-attachments/assets/b3fdbfc0-8e81-48e1-b63a-6a8d8867aa50" />



