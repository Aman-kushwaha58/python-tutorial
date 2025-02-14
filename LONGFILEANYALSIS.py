import re

def extract_usernames(log_data):
    return re.findall(r'User: (\w+)', log_data)

def extract_unique_ips(log_data):
    return set(re.findall(r'IP: ([\d\.]+)', log_data))

def count_failed_attempts(log_data):
    return len(re.findall(r'Status: FAILED', log_data))

log_data = """
[2025-02-10 14:23:45] User: Aman IP: 192.168.1.101 Status: SUCCESS
[2025-02-10 14:25:32] User: Bhupesh IP: 192.168.1.105 Status: FAILED
[2025-02-10 14:30:10] User: Jayant IP: 192.168.1.101 Status: FAILED
[2025-02-10 14:35:25] User: Nikhil IP: 192.168.1.200 Status: SUCCESS
"""

print("Usernames:", extract_usernames(log_data))
print("Unique IPs:", extract_unique_ips(log_data))
print("Failed Login Attempts:", count_failed_attempts(log_data))
