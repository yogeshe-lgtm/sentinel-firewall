# Sentinel Firewall CLI Guide

## Available Commands

The Sentinel Firewall CLI provides an easy-to-use command-line interface to control and monitor the firewall.

---

## Start Firewall

```bash
python3 src/main.py start# Sentinel Firewall CLI Guide

## Available Commands

The Sentinel Firewall CLI provides an easy-to-use command-line interface to control and monitor the firewall.

---

## Start Firewall

##```bash

python3 src/main.py start

##Starts the Sentinel Firewall service.

##Stop Firewall

python3 src/main.py stop

##Stops the Sentinel Firewall service.

##Firewall Status

python3 src/main.py status

##Displays the current firewall status, version, and configuration information.

##Monitor TrafficMonitor Traffic

python3 src/main.py monitor

##Displays live network traffic monitoring.

##(Currently under development. Packet monitoring will be implemented in future phases.)

View Logs
python3 src/main.py logs

Displays firewall security logs.

(Log management will be implemented in future phases.)

Manage Rules
python3 src/main.py rules


Future CLI Commands

The following commands will be added in future versions:

sentinel add-rule
sentinel delete-rule
sentinel whitelist
sentinel blacklist
sentinel export
sentinel config

These commands will provide advanced firewall management capabilities.

Version

Current Version: 0.1.0

Project: Sentinel Firewall
Manages firewall security rules.

(Rule engine will be implemented in future phases.)


