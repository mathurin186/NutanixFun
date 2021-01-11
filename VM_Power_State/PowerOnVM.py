#! python3

"""
Developed by Mathurin www.github.com/mathurin186
"""

import paramiko
import sys
import config

username = sys.argv[1]
password = sys.argv[2]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.48.2.15', port=22, username=username, password=password)
stdin, stdout, stderr = client.exec_command("acli vm.off cbd69a63-c0a1-404c-969a-9816e085372f && acli vm.off b637a621-6cf2-442c-a513-5caeb108e96f && acli vm.off 28d4c186-c05c-4709-814f-eb635b4f269d")
lines = stdout.read()

print(lines)
client.close()

