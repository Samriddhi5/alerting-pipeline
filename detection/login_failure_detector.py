import json
from datetime import datetime, timedelta
from collections import defaultdict

with open("logs/sample_log.json") as f:
    logs = json.load(f)

threshold = 3
window = timedelta(minutes=5)
failures = defaultdict(list)

alerts = []

for event in logs:
    if event["action"] == "login_failed":
        key = (event["user"], event["ip"])
        timestamp = datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
        failures[key].append(timestamp)
        failures[key] = [ts for ts in failures[key] if timestamp - ts <= window]
        if len(failures[key]) >= threshold:
            alerts.append(f"⚠️ Alert: {key[0]} failed login >{threshold} times from {key[1]}")

with open("alerts/alerts.txt", "w") as f:
    for alert in alerts:
        f.write(alert + "\n")

print("Alerting completed. See alerts/alerts.txt")
