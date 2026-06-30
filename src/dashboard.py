"""
Sentinel Firewall Dashboard
"""

from rich.console import Console
from rich.table import Table

console = Console()


def show_dashboard(stats):
    table = Table(title="Sentinel Firewall Dashboard")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Status", "ACTIVE")
    table.add_row("Total Packets", str(stats["total"]))
    table.add_row("Allowed", str(stats["allowed"]))
    table.add_row("Blocked", str(stats["blocked"]))
    table.add_row("TCP", str(stats["tcp"]))
    table.add_row("UDP", str(stats["udp"]))
    table.add_row("ICMP", str(stats["icmp"]))

    console.clear()
    console.print(table)
