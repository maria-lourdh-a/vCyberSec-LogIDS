# vCyberSec-LogIDS

## Overview
This project implements a custom log-based intrusion detection system (IDS) to detect SSH brute-force attacks from Linux authentication logs.

## Detection Logic
- Parses authentication log file
- Counts failed login attempts per IP address
- Triggers alert if attempts exceed defined threshold

## Technologies Used
- Python
- Regular Expressions
- Log Analysis

## How to Run

1. Ensure Python is installed
2. Place log_ids.py and sample_auth.log in the same directory
3. Run:

python log_ids.py

## Sample Output

---- Brute Force Detection Report ----
[ALERT] Possible Brute Force from 192.168.1.10 | Attempts: 5


