# Sentinel Firewall

A Python-based intelligent personal firewall for Kali Linux that monitors live network traffic, analyzes packets, detects suspicious activity, and logs security events.

## Features

- Live packet monitoring
- Rule-based packet filtering
- Port scan detection
- Packet flood detection
- SQLite event logging
- YAML configuration
- Rich CLI dashboard
- CSV report generation
- JSON rule management

## Technologies Used

- Python 3.13
- Scapy
- Typer
- Rich
- SQLite3
- PyYAML
- Pandas

## Installation

```bash
git clone <repository-url>
cd sentinel-firewall

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python3 src/main.py monitor
```

## Available Commands

```bash
python3 src/main.py start
python3 src/main.py monitor
python3 src/main.py status
python3 src/main.py logs
python3 src/main.py config
python3 src/main.py report
python3 src/main.py summary
```

## Project Structure

```
config/
database/
docs/
logs/
rules/
src/
tests/
```

## License

MIT License
