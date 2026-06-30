# Rule Engine

## Overview

The Rule Engine is responsible for analyzing packets and deciding whether traffic should be allowed or blocked.

## Supported Rules

- IP blocking
- Port blocking
- Protocol blocking
- Allow rules
- Block rules

## Rule Storage

Rules are stored in:

rules/rules.json


## Decision Process

1. Packet enters firewall
2. Packet information is extracted
3. Rules are checked
4. Action is returned

Possible actions:

- ALLOW
- BLOCK
