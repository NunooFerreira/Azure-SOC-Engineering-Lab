# Runbook: Onboard a Log Source (Linux syslog via AMA / DCR)

## Objectivo
Onboardar uma VM Linux como fonte de logs para o Log Analytics Workspace (LAW) e garantir que os eventos syslog chegam a Microsoft Sentinel.

## Pré-requisitos
- Conta Azure com permissões para criar/editar VMs e recursos de Monitor/Sentinel.
- Resource Group: `RG-SOC-Lab` (exemplo).
- Workspace: `LAW-SOC` (exemplo).
- VM Linux criada (ex.: `soc-linux-vm`) com acesso SSH.

## Passos (UI — Azure Portal)

### 1. Verificar Resource Group e Workspace
1. Abrir https://portal.azure.com  
2. Procurar **Resource groups** → confirmar `RG-SOC-Lab`.  
3. Procurar **Log Analytics workspaces** → confirmar `LAW-SOC`.

### 2. Criar / confirmar VM Linux
1. Virtual Machines → confirmar `soc-linux-vm` (Ubuntu 22.04).  
2. Notas: garantir Public IP (temporário), Auto-shutdown ON.

### 3. Criar Data Collection Rule (DCR)
1. Azure Monitor → **Data Collection Rules** → **+ Create**.  
2. Basics: subscription, RG `RG-SOC-Lab`, name `dcr-syslog-linux`, Platform: Linux.  
3. Resources → **Add resources** → seleccionar `soc-linux-vm` → Add.  
4. Collect & Deliver → **Add data source** → **Linux Syslog**.  
   - Facilities: `auth`, `authpriv`, `daemon`, `user`, `syslog`.  
   - Severity: `Info, Notice, Warning, Error, Critical`.  
5. Destination → seleccionar `LAW-SOC`.  
6. Review + Create → Create.

### 4. Verificar agente e ingestão
1. Aguardar 2–10 minutos.  
2. SSH para VM:
   ```bash
   ssh socadmin@<PUBLIC_IP>
   sudo systemctl status azuremonitoragent
   tail -n 20 /var/log/syslog
```
   
3. No Portal: Log Analytics Workspace (LAW-SOC) → Logs → correr:
```
Syslog
| where TimeGenerated > ago(30m)
| sort by TimeGenerated desc
```
