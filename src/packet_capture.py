"""
Sentinel Firewall
Packet Capture Module
"""
from dashboard import show_dashboard
from scapy.all import sniff
from firewall import Firewall
from packet_analyzer import analyze_packet
from statistics import TrafficStatistics


stats = TrafficStatistics()
firewall = Firewall()

def process_packet(packet):
    try:
        info = analyze_packet(packet)

        action = firewall.process_packet(info)

        if action is None:
            action = "BLOCK"

        stats.update(info, action)
        show_dashboard(stats.get_statistics())

        print("\n--------------------------------")
        print(f"Time        : {info['time']}")
        print(f"Source      : {info['source']}")
        print(f"Destination : {info['destination']}")
        print(f"Protocol    : {info['protocol']}")

        if info["source_port"]:
            print(
                f"Ports       : {info['source_port']} → {info['destination_port']}"
            )

        print(f"Size        : {info['size']} bytes")

    except Exception as e:
        import traceback

        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("===========================\n")



def start_capture():

    print(
        "Starting Sentinel Firewall packet monitoring..."
    )


    sniff(
    prn=process_packet,
    store=False,
    filter="ip"
    )
