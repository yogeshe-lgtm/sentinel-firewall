"""
Sentinel Firewall
Decision Display Module
"""

from logger import write_log



def display_decision(packet, action):


    message = (

        f"{action} | "

        f"{packet['protocol']} | "

        f"{packet['source']} -> "

        f"{packet['destination']}"

    )


    write_log(message)



    print("\n================================")
    print(" SENTINEL FIREWALL DECISION")
    print("================================")


    print(
        f"Source      : {packet['source']}"
    )

    print(
        f"Destination : {packet['destination']}"
    )

    print(
        f"Protocol    : {packet['protocol']}"
    )


    if packet["destination_port"]:

        print(
            f"Port        : {packet['destination_port']}"
        )


    print(
        f"Decision    : {action}"
    )


    print("================================")
