"""
Sentinel Firewall Configuration Loader
"""

import yaml

CONFIG_FILE = "config/firewall.yaml"


def load_config():
    """
    Load configuration from YAML file.
    """

    with open(CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)

    return config
