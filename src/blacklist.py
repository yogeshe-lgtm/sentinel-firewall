"""
Sentinel Firewall
Blacklist Manager
"""

import json

BLACKLIST_FILE = "data/blacklist.json"


def load_blacklist():
    """Load blocked IPs from disk."""

    try:
        with open(BLACKLIST_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"blocked_ips": []}


def save_blacklist(data):
    """Save blocked IPs."""

    with open(BLACKLIST_FILE, "w") as file:
        json.dump(data, file, indent=4)


def is_blocked(ip):
    """Check if IP is already blocked."""

    data = load_blacklist()
    return ip in data["blocked_ips"]


def block_ip(ip):
    """Add an IP to the blacklist."""

    data = load_blacklist()

    if ip not in data["blocked_ips"]:
        data["blocked_ips"].append(ip)
        save_blacklist(data)
