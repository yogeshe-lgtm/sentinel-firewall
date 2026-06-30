# Sentinel Firewall Architecture


                 Network Traffic
                       |
                       |
                       v

              Packet Capture
                 (Scapy)

                       |
                       |

              Packet Analyzer

                       |
                       |

              Threat Detection Engine
                 /           \
                /             \
        Port Scan        Packet Flood


                       |
                       |

              Rule Engine

                       |
              +--------+--------+
              |                 |
            ALLOW             BLOCK


                       |
                       |

              Logging System
                 |
                 |
              SQLite Database

                       |
                       |

              Reporting System
                 |
                 |
              CSV Reports
```

Save.

---

# STEP 5 — Improve README

Open:

```bash
nano README.md
```

Add this at the bottom:

````markdown

# Screenshots

## Live Monitoring Dashboard

![Dashboard](screenshots/dashboard.png)


## Architecture

![Architecture](docs/architecture.png)


# Security Capabilities

## Traffic Monitoring

Captures live network packets using Scapy.

## Rule Based Filtering

Supports custom rules:

- Protocol filtering
- Port filtering
- Allow/block actions

## Threat Detection

Detects:

- Port scanning attempts
- Packet flooding behavior
- Suspicious traffic patterns


# Future Improvements

- Web dashboard
- Machine learning based detection
- Automatic IP reputation checking
- GeoIP threat mapping
- Windows support
