"""
Sentinel Firewall
Traffic Monitoring Module
"""

from packet_capture import start_capture


def start_monitor():

    print(
        """
===============================
 Sentinel Firewall Monitor
===============================
        """
    )

    start_capture()
