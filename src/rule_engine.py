"""
Sentinel Firewall
Rule Engine

Responsible for making
allow/block decisions.
"""


from .rules_manager import load_rules



class RuleEngine:


    def __init__(self):

        self.rules = load_rules()



    def check_packet(self, packet):

        rules = self.rules["rules"]


        for rule in rules:


            # Protocol check

            if (
                rule.get("protocol")
                and
                rule["protocol"] != packet["protocol"]
            ):

                continue



            # Port check

            if (
                rule.get("port")
                and
                rule["port"] != packet["destination_port"]
            ):

                continue



            return rule["action"]



        return self.rules["default_policy"]
