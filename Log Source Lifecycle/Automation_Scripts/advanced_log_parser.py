#!/usr/bin/env python3
import re
import json
import datetime

# Read last syslog line
with open("/var/log/syslog", "r") as f:
    lines = f.readlines()
    raw_log = lines[-1].strip()

print("=== RAW LOG INPUT ===")
print(raw_log)
print("======================\n")

# Regex that extracts timestamp, hostname, process, message
pattern = r"^(\w{3}\s+\d{1,2}\s[\d:]{8})\s(\S+)\s(\S+):\s(.*)$"
match = re.match(pattern, raw_log)

if not match:
    print("❌ ERROR: Log format does NOT match expected Linux syslog pattern.")
    exit()

timestamp, hostname, process, message = match.groups()

# Extract user + IP if present (simulate auth parsing)
user_match = re.search(r"user=([A-Za-z0-9_-]+)", raw_log)
ip_match = re.search(r"ip=([\d\.]+)", raw_log)

user = user_match.group(1) if user_match else None
ip = ip_match.group(1) if ip_match else None

print("=== PARSED OUTPUT ===")
print(f"Timestamp : {timestamp}")
print(f"Hostname  : {hostname}")
print(f"Process   : {process}")
print(f"Message   : {message}")
print(f"User      : {user}")
print(f"IP        : {ip}")
print("=====================\n")

# Build normalized JSON object (like a SIEM would)
normalized = {
    "timestamp": timestamp,
    "hostname": hostname,
    "process": process,
    "message": message,
    "user": user,
    "ip_address": ip,
    "log_source_type": "linux-syslog",
    "ingested_at": datetime.datetime.utcnow().isoformat() + "Z"
}

print("=== NORMALIZED JSON ===")
print(json.dumps(normalized, indent=4))
print("========================")
