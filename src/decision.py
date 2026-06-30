"""
Sentinel Firewall
Decision Display Module
"""


def display_decision(packet, action):

    print("\n================================")
    print(" SENTINEL FIREWALL DECISION")
    print("================================")


    print(f"Source      : {packet['source']}")
    print(f"Destination : {packet['destination']}")
    print(f"Protocol    : {packet['protocol']}")


    if packet["destination_port"]:
        print(
            f"Port        : {packet['destination_port']}"
        )


    print(f"Decision    : {action}")

    print("================================")
