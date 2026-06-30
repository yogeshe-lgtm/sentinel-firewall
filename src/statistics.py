"""
Sentinel Firewall
Traffic Statistics Module
"""


class TrafficStatistics:

    def __init__(self):

        self.total_packets = 0

        self.protocols = {
            "TCP": 0,
            "UDP": 0,
            "ICMP": 0,
            "UNKNOWN": 0
        }


    def update(self, packet_info):

        self.total_packets += 1

        protocol = packet_info["protocol"]

        if protocol in self.protocols:

            self.protocols[protocol] += 1

        else:

            self.protocols["UNKNOWN"] += 1



    def display(self):

        print("\n====== Traffic Statistics ======")

        print(
            f"Total Packets : {self.total_packets}"
        )


        for protocol, count in self.protocols.items():

            print(
                f"{protocol:<10}: {count}"
            )
