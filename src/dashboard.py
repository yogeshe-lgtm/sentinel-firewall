"""
Sentinel Firewall Live Dashboard
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def show_dashboard(stats):

    console.clear()

    table = Table(title="Sentinel Firewall v1.0")

    table.add_column("Metric", style="cyan", width=20)
    table.add_column("Value", style="green", width=15)

    table.add_row("Status", "ACTIVE")
    table.add_row("Total Packets", str(stats["total"]))
    table.add_row("Allowed", str(stats["allowed"]))
    table.add_row("Blocked", str(stats["blocked"]))
    table.add_row("TCP", str(stats["tcp"]))
    table.add_row("UDP", str(stats["udp"]))
    table.add_row("ICMP", str(stats["icmp"]))

    console.print(table)

    console.print(
        Panel(
            "[bold green]Monitoring Live Network Traffic...[/bold green]",
            title="Status"
        )
    )
