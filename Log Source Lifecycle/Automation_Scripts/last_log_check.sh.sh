LAST_LOG=$(sudo tail -n 1 /var/log/syslog | awk '{print $1, $2, $3}')
echo "Last syslog entry: $LAST_LOG"
