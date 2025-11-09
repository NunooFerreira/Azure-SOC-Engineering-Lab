# Runbook: Onboard a Linux Log Source (Syslog via AMA / DCR)

## Purpose
This runbook explains how to onboard a Linux virtual machine and configure it as a log source for the Log Analytics Workspace (LAW), ensuring that syslog events are ingested into Microsoft Sentinel.

## Prerequisites
- Azure account with permissions to create/modify VMs and monitoring resources.
- Resource Group: `RG-SOC-Lab` (example).
- Log Analytics Workspace: `LAW-SOC` (example).
- Linux VM created (e.g., `soc-linux-vm`) with SSH access.

## Steps (Azure Portal UI)

---

### 1. Verify Resource Group and Workspace
1. Open https://portal.azure.com  
2. Navigate to **Resource groups** → confirm `RG-SOC-Lab`.  
3. Navigate to **Log Analytics workspaces** → confirm `LAW-SOC`.

---

### 2. Create / Validate the Linux VM
1. Go to **Virtual Machines** → confirm `soc-linux-vm` exists (Ubuntu 22.04 recommended).  
2. Notes: ensure the VM has a Public IP (temporary is fine) and Auto-shutdown enabled.

---

### 3. Create a Data Collection Rule (DCR)
1. Go to **Azure Monitor** → **Data Collection Rules** → **+ Create**.  
2. **Basics**  
   - Subscription: your subscription  
   - Resource Group: `RG-SOC-Lab`  
   - Name: `dcr-syslog-linux`  
   - Platform: **Linux**  
3. **Resources** → click **Add resources** → select `soc-linux-vm` → Add.  
4. **Collect & Deliver** → click **Add data source** → choose **Linux Syslog**.  
   - Facilities: `auth`, `authpriv`, `daemon`, `user`, `syslog`  
   - Severities: `Info`, `Notice`, `Warning`, `Error`, `Critical`  
5. **Destination** → select `LAW-SOC`.  
6. Click **Review + Create** → **Create**.

---

### 4. Verify the Agent and Log Ingestion
1. Wait 2–10 minutes for the Azure Monitor Agent (AMA) to initialise.  
2. SSH into the VM:
   ```bash
   ssh socadmin@<PUBLIC_IP>
   sudo systemctl status azuremonitoragent
   tail -n 20 /var/log/syslog
```
3. In the Azure Portal, go to LAW-SOC → Logs and run:

Syslog
| where TimeGenerated > ago(30m)
| sort by TimeGenerated desc

If there are logs, onboarding is successful.