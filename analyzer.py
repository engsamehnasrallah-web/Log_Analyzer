import os
import re

LOG_FILE_PATH = "sample_logs/auth.log"
pattern = r"for (\w+) from ([\d.]+)"
accepted_counter = 0
failed_counter = 0

if not os.path.exists(LOG_FILE_PATH):
    print("Error : Log file not found.")
    exit()

try:
    with open(LOG_FILE_PATH, 'r') as file:
        log_entries = file.readlines()
    total_log_entries = len(log_entries)
    
    for line in log_entries:
        if("Failed password" in line):
            failed_counter += 1
        elif("Accepted password" in line):
            accepted_counter += 1
        if "Failed password" in line or "Accepted password" in line:
            match = re.search(pattern, line)
            if match:
                user = match.group(1)
                ip_address = match.group(2)
        print(f"User: {user}, IP Address: {ip_address}")
    
    print("=" * 40)
    print("              SEC Log Analyzer")
    print("=" * 40 + "\n")
    print("✓ Log file loaded successfully.\n")
    print(f"Total Log Entries       : {total_log_entries}")
    print(f"Failed Login Attempts   : {failed_counter}")
    print(f"Successful Logins       : {accepted_counter}")


except PermissionError:
    print("Permission denied.")
    exit()
except Exception as error:
    print(f"Unexpected error: {error}")
    exit()

input("\nPress Enter to exit...")