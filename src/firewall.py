"""
Sentinel Firewall Controller
"""


from rule_engine import RuleEngine
from decision import display_decision


class Firewall:


    def __init__(self):

        self.rule_engine = RuleEngine()



    def process_packet(self, packet):

        decision = self.rule_engine.check_packet(packet)

        display_decision(
            packet,
            decision
        )

        return decision
