"""
Traffic Statistics
"""


class TrafficStatistics:

    def __init__(self):

        self.total = 0
        self.allowed = 0
        self.blocked = 0

        self.tcp = 0
        self.udp = 0
        self.icmp = 0

    def update(self, packet, action):

        self.total += 1

        protocol = packet["protocol"]

        if protocol == "TCP":
            self.tcp += 1

        elif protocol == "UDP":
            self.udp += 1

        elif protocol == "ICMP":
            self.icmp += 1

        if action == "ALLOW":
            self.allowed += 1

        else:
            self.blocked += 1

    def get_statistics(self):

        return {
            "total": self.total,
            "allowed": self.allowed,
            "blocked": self.blocked,
            "tcp": self.tcp,
            "udp": self.udp,
            "icmp": self.icmp,
        }
