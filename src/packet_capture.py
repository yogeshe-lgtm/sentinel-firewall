"""
Sentinel Firewall
Packet Capture Module
"""

from scapy.all import sniff
from firewall import Firewall
from packet_analyzer import analyze_packet
from statistics import TrafficStatistics


stats = TrafficStatistics()
firewall = Firewall()

def process_packet(packet):

    info = analyze_packet(packet)
    firewall.process_packet(info)

    stats.update(info)


    print("\n--------------------------------")

    print(
        f"Time        : {info['time']}"
    )

    print(
        f"Source      : {info['source']}"
    )

    print(
        f"Destination : {info['destination']}"
    )

    print(
        f"Protocol    : {info['protocol']}"
    )


    if info["source_port"]:

        print(
            f"Ports       : {info['source_port']} → {info['destination_port']}"
        )


    print(
        f"Size        : {info['size']} bytes"
    )



def start_capture():

    print(
        "Starting Sentinel Firewall packet monitoring..."
    )


    sniff(
        prn=process_packet,
        store=False
    )
