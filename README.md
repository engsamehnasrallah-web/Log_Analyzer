# SEC Log Analyzer 

A Python-based security tool that analyzes Linux authentication logs to detect failed login attempts, successful logins, and suspicious activities.

---

## Overview

SEC Log Analyzer is a lightweight log analysis tool designed to parse Linux authentication logs and provide useful and provide useful security insights. The project is built incrementally using an Agile sprint-based approach.

---

## Features

### Sprint 1
- Project initialization
- Professional project structure 
- Error handling for missing log files

### Sprint 2
- Load Linux authentication log files
- Count total log entries
- File validation and exception handling

### Sprint 3
- Detect failed login attempts
- Detect successful login attempts
- Display login statistics

### Sprint 4
- Detect failed login attempts
- Extract source IP addresses
- Regular Expression (Regex) based parsing
- Improved authentication event analysis

---

## Screenshots
![Sprint 4 Output](screenshots/Sprint_4.png)

---

## Technologies

- Python
- Regular Expressions (Regex)
- File Handling
- Exception Handling

---

## Project Structure

```text
Log_Analyzer/
│
├── analyzer.py
├── sample_logs/
│   └── auth.log
├── reports/
├── screenshots/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

# 📌 Roadmap

### Upcoming (Sprint 5)

- Refactor project into multiple modules
- Introduce cleaner architecture
- Separate parsing, analysis, and reporting logic

---

## Current Status

📊 **v0.4.0**
🟢 Sprint 3 Completed

---

## Upcoming Features

- JSON report export
- HTML Reports
- Brute-force detection
- Suspicious IP Ranking
- Command-line Arguments
- Unit Testing