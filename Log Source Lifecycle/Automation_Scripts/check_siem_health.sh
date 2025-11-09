#!/bin/bash
echo "==== Checking Azure Monitor Agent status ===="
systemctl status azuremonitoragent | grep Active

echo ""
echo "==== Last 10 syslog entries ===="
tail -n 10 /var/log/syslog
