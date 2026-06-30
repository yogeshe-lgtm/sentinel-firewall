"""
Sentinel Firewall
Rules Manager

Loads firewall rules from JSON.
"""

import json


RULE_FILE = "rules/rules.json"



def load_rules():

    with open(RULE_FILE,"r") as file:

        data = json.load(file)

    return data
