# 🔔 Alerting Pipeline Project

This project is a simple Python-based alerting pipeline for detecting suspicious behavior in log files. It simulates a basic SIEM detection process, reading JSON log files, applying detection logic, and outputting alerts.

---

## 📁 Folder Structure

- `logs/` – Contains sample input logs
- `detection/` – Detection logic script
- `alerts/` – Output alert file
- `config/` – Configurable thresholds

---

## 🚀 How to Run

```bash
python detection/login_failure_detector.py
```

---

## 💡 Detection Logic

The rule flags any user with **more than 3 failed logins from the same IP within 5 minutes**.

- You can configure this in `config/thresholds.json` (for future extension).
- Alerts will be written to `alerts/alerts.txt`.

---

## 🔧 Expand This Project

- Add Slack/email alerting
- Integrate with Filebeat or Kafka for real-time log streaming
- Add more detection rules (file hash matching, geolocation anomalies, etc.)
- Convert logic to use Sigma rules

---

## 📄 License

MIT
