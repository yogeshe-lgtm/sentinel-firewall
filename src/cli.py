"""
Sentinel Firewall CLI Module
"""

import typer
from rich.console import Console

from config import FIREWALL_NAME, VERSION


app = typer.Typer(
    help="Sentinel Firewall - Intelligent Linux Firewall"
)

console = Console()


@app.command()
def start():
    """
    Start firewall
    """

    console.print(
        "[green]Firewall started successfully[/green]"
    )


@app.command()
def stop():
    """
    Stop firewall
    """

    console.print(
        "[red]Firewall stopped[/red]"
    )


@app.command()
def status():
    """
    Show firewall status
    """

    console.print(
        f"""
        {FIREWALL_NAME}

        Version: {VERSION}

        Status: ACTIVE
        """
    )


@app.command()
def monitor():
    """
    Monitor network traffic
    """

    from monitor import start_monitor

    start_monitor()


@app.command()
def logs():
    """
    View logs
    """

    console.print(
        "[blue]Logging system coming soon...[/blue]"
    )


@app.command()
def rules():
    """
    Manage firewall rules
    """

    console.print(
        "[cyan]Rule engine coming soon...[/cyan]"
    )


@app.command()
def stats():
    """
    Show firewall statistics
    """

    console.print(
        "[magenta]Statistics module coming soon...[/magenta]"
    )
