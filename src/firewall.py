"""
Sentinel Firewall Controller
"""

from rule_engine import RuleEngine
from decision import display_decision
from threat_detector import ThreatDetector


class Firewall:
    def __init__(self):
        self.rule_engine = RuleEngine()
        self.threat_detector = ThreatDetector()

    def process_packet(self, packet):
        # Check for suspicious activity first
        threat = self.threat_detector.analyze(packet)

        if threat == "BLOCKED":
            display_decision(packet, "BLOCKED (Blacklisted)")
            return "BLOCKED"

        elif threat == "PORT_SCAN":
            display_decision(packet, "BLOCKED (Port Scan)")
            return "BLOCKED"

        elif threat == "PACKET_FLOOD":
            display_decision(packet, "BLOCKED (Packet Flood)")
            return "BLOCKED"

        # No threat detected, apply firewall rules
        decision = self.rule_engine.check_packet(packet)

        display_decision(packet, decision)

        return decision
