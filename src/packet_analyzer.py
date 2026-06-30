"""
Sentinel Firewall
Packet Analyzer Module

Responsible for extracting information
from captured packets.
"""

from datetime import datetime

from scapy.layers.inet import IP, TCP, UDP, ICMP


def analyze_packet(packet):
    """
    Extract packet information
    """

    packet_info = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "source": None,
        "destination": None,
        "protocol": "UNKNOWN",
        "source_port": None,
        "destination_port": None,
        "size": len(packet)
    }


    # Check IP layer
    if packet.haslayer(IP):

        ip_layer = packet[IP]

        packet_info["source"] = ip_layer.src
        packet_info["destination"] = ip_layer.dst


    # TCP Detection
    if packet.haslayer(TCP):

        packet_info["protocol"] = "TCP"

        packet_info["source_port"] = packet[TCP].sport
        packet_info["destination_port"] = packet[TCP].dport


    # UDP Detection
    elif packet.haslayer(UDP):

        packet_info["protocol"] = "UDP"

        packet_info["source_port"] = packet[UDP].sport
        packet_info["destination_port"] = packet[UDP].dport


    # ICMP Detection
    elif packet.haslayer(ICMP):

        packet_info["protocol"] = "ICMP"


    return packet_info
