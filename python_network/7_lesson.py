import re

ip = "192.168.1.1"

if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
    print("Valid!")