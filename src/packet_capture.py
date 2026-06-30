"""
Sentinel Firewall
Packet Capture Module

Responsible for capturing and analyzing network packets.
"""

from scapy.all import sniff


packet_count = 0


def analyze_packet(packet):
    """
    Analyze captured packets
    """

    global packet_count

    packet_count += 1

    print("\n----------------------------")
    print(f"Packet Number: {packet_count}")

    print(packet.summary())

    print("----------------------------")


def start_capture():
    """
    Start live packet capture
    """

    print("Starting packet capture...")

    sniff(
        prn=analyze_packet,
        store=False
    )
