
"""
Sentinel Firewall Alert System
"""

from rich.console import Console

console = Console()


def show_alert(threat_type, ip):
    console.print()
    console.print("[bold red]🚨 SECURITY ALERT[/bold red]")
    console.print(f"[red]Threat : {threat_type}[/red]")
    console.print(f"[red]Source : {ip}[/red]")
    console.print("[yellow]Action : IP Added to Blacklist[/yellow]")
    console.print()
