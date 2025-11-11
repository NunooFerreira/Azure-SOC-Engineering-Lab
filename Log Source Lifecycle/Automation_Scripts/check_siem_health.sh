#!/bin/bash

echo "==============================================="
echo "      Azure Monitor Agent - Basic Health Check"
echo "==============================================="

echo ""
echo "==== Checking AMA service status ===="
systemctl status azuremonitoragent --no-pager | grep Active

echo ""
echo "==== Checking Heartbeat logs ===="
grep -i "heartbeat" /var/log/syslog | tail -n 5 || \
    echo "No recent AMA heartbeat entries found."

echo ""
echo "==== Last 10 syslog events (context only) ===="
tail -n 10 /var/log/syslog

echo ""
echo "Basic health check complete."
