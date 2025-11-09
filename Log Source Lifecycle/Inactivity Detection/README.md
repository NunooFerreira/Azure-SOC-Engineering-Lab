# Decommissioning a Log Source in Azure Log Analytics

This document explains the process used to verify whether a log source is still sending data to Azure Log Analytics and determine if it should be decommissioned.  
It also includes a brief explanation of the Python script created for this purpose.

---

## ✅ Overview

During the lifecycle of a SOC environment, some log sources become inactive due to system removal, reinstallation, migration, or misconfiguration.  
To maintain visibility and avoid unnecessary costs, we created a method to:

1. Query Azure Log Analytics for recent logs  
2. Detect when a log source stops sending events  
3. Alert the analyst so the log source can be reviewed or decommissioned  

This is part of the **Log Source Lifecycle Management** process.

---

## 🧰 Requirements

To run the monitoring script on the Linux VM:

- Python 3  
- `azure-monitor-query`  
- `azure-identity`  
- Log Analytics Workspace **Customer ID**  
- Log Analytics Workspace **Primary Shared Key**

Install required Python modules:

```bash
pip install azure-monitor-query azure-identity
```

## Authentication

The script uses:

1 - Workspace ID (Customer ID)

2 - Primary Shared Key

Obtain these with Azure CLI (on your admin machine):
```
az monitor log-analytics workspace show \
  -g <resource-group> -n <workspace-name> --query customerId

az monitor log-analytics workspace get-shared-keys \
  -g <resource-group> -n <workspace-name> --query primarySharedKey

```

## Python Script:
Then created a Python Script that connects to Azure Log Analytics using Workspace ID + Shared Key and:

- Runs a KQL query.

- Searches for logs from the last 24 hours

- If logs exist -- "Logs are comming."

- If no logs exist -- "Missing Logs... The device stoped sending logs for 5 minutos!"


The script (check_logs.py) uses Azure’s Python SDK:

LogsQueryClient — sends KQL queries to Log Analytics

WorkspaceSharedKeyCredential — authenticates using the workspace key

query_workspace() — retrieves log data


## Output:

When there are logs comming: 

--- image.


After I stoped the agent on the VM and waited 5 minutes: 


--- image.