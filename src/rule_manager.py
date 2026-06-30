"""
Sentinel Firewall Rule Manager
"""

import json
from pathlib import Path

RULE_FILE = Path("rules/rules.json")


class RuleManager:

    def load(self):
        with open(RULE_FILE, "r") as f:
            return json.load(f)

    def save(self, rules):
        with open(RULE_FILE, "w") as f:
            json.dump(rules, f, indent=4)

    def list_rules(self):
        return sorted(
            self.load(),
            key=lambda r: r["priority"],
            reverse=True
        )

    def add_rule(self, rule):
        rules = self.load()
        rules.append(rule)
        self.save(rules)

    def delete_rule(self, rule_id):
        rules = self.load()
        rules = [r for r in rules if r["id"] != rule_id]
        self.save(rules)
