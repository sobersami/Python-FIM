# Python-Based File Integrity Monitoring (FIM) Tool

## 📖 Overview
A lightweight File Integrity Monitoring tool developed in Python, designed to detect unauthorized changes, deletions, or new file creation events within a monitored directory by calculating and comparing file hashes using SHA-512.

## 🚀 Features
- **Baseline Hash Collection:** Capture the initial SHA-512 hash state of all files in a target directory.
- **Real-Time Monitoring:** Continuously monitors the directory for file changes, deletions, and additions.
- **SHA-512 Hashing:** Ensures strong cryptographic hash verification for file integrity.
- **Console Alerts:** Instant feedback for compromised, deleted, or new files via terminal output.
- **Python Automation:** Modular functions for baseline creation, file hashing, and continuous integrity checks.

## 🔧 Usage
1. Run `fim.py`.
2. Choose option `A` to collect a baseline or `B` to begin monitoring.
3. The script will notify you via console output of:
   - New file creation
   - File modifications
   - File deletions

## 📦 Technologies
- Python 3.x
- hashlib
- os
- time

## 📌 Future Improvements
- Log file creation for persistent records.
- Email or push notifications for incident alerts.
- Recursive directory monitoring.
- JSON or CSV baseline export.


