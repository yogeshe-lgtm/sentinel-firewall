
"""
Sentinel Firewall CLI Module
"""
from report import generate_report
import typer
from rich.console import Console
from config import FIREWALL_NAME, VERSION
from config_loader import load_config
from report import generate_report,generate_summary

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
    View firewall logs
    """

    try:

        with open("logs/firewall.log","r") as file:

            console.print(
                file.read()
            )


    except FileNotFoundError:

        console.print(
            "[yellow]No logs available[/yellow]"
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
@app.command()
def config():
    """
    Display current firewall configuration.
    """

    config = load_config()

    console.print(config)
@app.command()
def report():
    """
    Generate firewall report
    """

    generate_report()
@app.command()
def summary():
    """
    Display firewall summary
    """

    generate_summary()
