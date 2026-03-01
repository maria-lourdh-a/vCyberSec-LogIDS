import re
from collections import defaultdict

LOG_FILE = "sample_auth.log"
THRESHOLD = 5

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] += 1

import datetime

print("---- Brute Force Detection Report ----\n")

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ALERT: Possible Brute Force from {ip} | Attempts: {count}")
