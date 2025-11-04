# Azure SOC Engineering Lab

This project demonstrates the end-to-end design and deployment of a **cloud-native Security Operations Center (SOC)** on **Microsoft Azure**.  
It includes the configuration of a honeypot virtual machine (VM), centralized log collection, SIEM integration with **Microsoft Sentinel**, log enrichment with geolocation data, and visualization of global attack sources through an interactive attack map.

The purpose of this lab is to simulate real-world SOC workflows — from telemetry ingestion and event analysis to visualization and threat detection — using modern cloud-native tools and security engineering principles.

---

## 🎯 Objectives

- Deploy a **Windows honeypot** VM in Azure to attract and capture malicious login attempts.
- Collect and centralize logs via **Log Analytics Workspace (LAW)**.
- Configure and enable **Microsoft Sentinel** as the SIEM for monitoring and correlation.
- Use **Azure Monitor Agent (AMA)** and **Data Collection Rules (DCR)** to forward Windows Security events.
- Enrich logs with **geolocation data** using Sentinel Watchlists.
- Visualize global attacker sources using a **Sentinel Workbook attack map**.
- Document the complete SOC engineering process, from setup to detection.

---

## 🧱 Architecture Overview

