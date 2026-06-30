"""
Sentinel Firewall
Threat Detection Engine
"""

import time
from alert import show_alert
from blacklist import block_ip, is_blocked


class ThreatDetector:
    """
    Detect suspicious network activity.
    """

    def __init__(self):

        # Stores activity for each source IP
        self.activity = {}

        # Detection thresholds
        self.packet_threshold = 50
        self.port_threshold = 20
        self.time_window = 10  # seconds

    def analyze(self, packet):

        source_ip = packet["source"]

        # Ignore already blocked IPs
        if is_blocked(source_ip):
            return "BLOCKED"

        current_time = time.time()

        if source_ip not in self.activity:
            self.activity[source_ip] = {
                "packets": 0,
                "ports": set(),
                "first_seen": current_time,
            }

        data = self.activity[source_ip]

        data["packets"] += 1

        port = packet.get("destination_port")

        if port:
            data["ports"].add(port)

        elapsed = current_time - data["first_seen"]

        # Reset counters after the time window expires
        if elapsed > self.time_window:
            data["packets"] = 1
            data["ports"] = set()

            if port:
                data["ports"].add(port)

            data["first_seen"] = current_time
            return "ALLOW"

        # Packet flood detection
        if data["packets"] >= self.packet_threshold:
            block_ip(source_ip)
            return "PACKET_FLOOD"

        # Port scan detection
        if len(data["ports"]) >= self.port_threshold:
            block_ip(source_ip)
            return "PORT_SCAN"

        return "ALLOW"
