# Log Source Inactivity Detection in Azure Log Analytics

This section documents the process I implemented to automatically verify whether a log source is still sending data to Azure Log Analytics.
The goal is to detect when a machine becomes inactive so that visibility gaps and telemetry blind spots can be avoided.

I also describe the Python script I created and tested to validate this monitoring workflow.
---

## Overview

A log source can stop sending logs for many reasons — such as the machine being shut down, misconfigured, reinstalled, or removed from the environment.
When this happens, the SOC loses visibility, which impacts detection and response capabilities.

To prevent this, I implemented an Inactivity Detection mechanism that automatically monitors the health of each log source.

The script performs the following tasks:

Queries Azure Log Analytics for the most recent logs from a specific machine
Detects when the machine stops sending data within a defined time window
Alerts me when inactivity is detected so I can investigate the machine or update the SOC documentation


---

## Authentication

The script uses:

1 - Workspace ID (Customer ID)

2 - Primary Shared Key

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

<img width="607" height="42" alt="image" src="https://github.com/user-attachments/assets/ac966e5b-f7d1-4468-a117-dfe106b4f0ab" />



After I stoped the agent on the VM and waited 5 minutes: 


<img width="601" height="40" alt="image" src="https://github.com/user-attachments/assets/f141e4f9-e77d-412b-b0b7-cd3e93569ad5" />
