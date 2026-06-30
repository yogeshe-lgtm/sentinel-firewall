"""
Sentinel Firewall
Rule Engine

Responsible for making
allow/block decisions.
"""

from rules_manager import load_rules


class RuleEngine:

    def __init__(self):
        self.reload_rules()

    def reload_rules(self):
        """Reload rules from rules.json"""
        self.rules = sorted(
            load_rules(),
            key=lambda r: r.get("priority", 0),
            reverse=True
        )

    def check_packet(self, packet):
        """
        Check whether a packet should be allowed or blocked.
        """

        for rule in self.rules:

            # Skip disabled rules
            if not rule.get("enabled", True):
                continue

            # Protocol check
            if (
                rule.get("protocol")
                and rule["protocol"] != packet["protocol"]
            ):
                continue

            # Port check
            if (
                rule.get("port")
                and rule["port"] != packet["destination_port"]
            ):
                continue

            # Matching rule found
            return rule["action"]

        # Default action
        return "ALLOW""""
Sentinel Firewall
Rule Engine

Responsible for making
allow/block decisions.
"""

from rules_manager import load_rules


class RuleEngine:

    def __init__(self):
        self.reload_rules()

    def reload_rules(self):
        """Reload rules from rules.json"""
        self.rules = sorted(
            load_rules(),
            key=lambda r: r.get("priority", 0),
            reverse=True
        )

    def check_packet(self, packet):
        """
        Check whether a packet should be allowed or blocked.
        """

        for rule in self.rules:

            # Skip disabled rules
            if not rule.get("enabled", True):
                continue

            # Protocol check
            if (
                rule.get("protocol")
                and rule["protocol"] != packet["protocol"]
            ):
                continue

            # Port check
            if (
                rule.get("port")
                and rule["port"] != packet["destination_port"]
            ):
                continue

            # Matching rule found
            return rule["action"]

        # Default action
        return "ALLOW"
