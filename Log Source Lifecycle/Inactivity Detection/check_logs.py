from azure.identity import AzureCliCredential
from azure.monitor.query import LogsQueryClient
from datetime import datetime, timedelta
import sys

# --------------- CONFIGURAÇÕES -----------------
WORKSPACE_ID = "0bb55dea-fdff-4b57-a365-6427cb01f963"   # teu workspace ID
MINUTES = 5  # intervalo de tempo para verificar logs
# ------------------------------------------------

credential = AzureCliCredential()
client = LogsQueryClient(credential)

query = """
Heartbeat
| where TimeGenerated > ago({}m)
""".format(MINUTES)

try:
    response = client.query_workspace(
        WORKSPACE_ID,
        query,
        timespan=timedelta(minutes=MINUTES)
    )

    if response.tables and len(response.tables[0].rows) > 0:
        print("Logs are comming.")
    else:
        print("Missing Logs... The device stoped sending logs for {} minutes!".format(MINUTES))

except Exception as e:
    print("Erro ao consultar o Log Analytics:", e)
    sys.exit(1)