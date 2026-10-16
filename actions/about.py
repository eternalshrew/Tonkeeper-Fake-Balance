# -*- coding: utf-8 -*-
"""About action — Features, supported assets, contact"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

from backend.ui import console


def action_about():
    console.print()
    console.print(Rule("[bold cyan]ABOUT[/]", style="cyan"))

    features_table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE)
    features_table.add_column("Feature", style="green")
    features_table.add_column("Status", justify="center")

    for feat in [
        "Custom balance for TON & Jettons",
        "50+ supported Jetton tokens",
        "Persistent across wallet restarts",
        "Screenshot-safe rendering",
        "Real-time USD value display",
        "Transaction history spoofing",
        "Multi-account support",
        "One-click apply / restore",
        "Auto-detect Tonkeeper installation",
        "API response interception",
        "Process-level memory patching",
        "No blockchain modification",
    ]:
        features_table.add_row(feat, "[green]+[/]")

    assets_table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE)
    assets_table.add_column("Category", style="green")
    assets_table.add_column("Assets", style="cyan")
    assets_table.add_row("Native", "TON")
    assets_table.add_row("Stablecoins", "USDT, USDC, DAI")
    assets_table.add_row("DeFi", "STON, JETTON, SCALE, UP")
    assets_table.add_row("Meme", "NOT, DOGS, HMSTR, CATI, MAJOR")
    assets_table.add_row("Liquid Staking", "stTON, tsTON, hTON")

    contact_table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE)
    contact_table.add_column("Channel", style="green")
    contact_table.add_column("Value", style="cyan")
    contact_table.add_row("Telegram", "JOIN OUR TELEGRAM CHAT")
    contact_table.add_row("TON Address", "UQCD...abc123")
    contact_table.add_row("Support", "GitHub Issues or Telegram")

    console.print(Panel(features_table, title="[bold] Features [/]", border_style="cyan", box=box.ROUNDED))
    console.print()
    console.print(Panel(assets_table, title="[bold] Supported Assets [/]", border_style="cyan", box=box.ROUNDED))
    console.print()
    console.print(Panel(contact_table, title="[bold] Contact [/]", border_style="cyan", box=box.ROUNDED))
    console.print()
    console.print("[bold cyan]Contribution:[/] Don't forget to put stars *")
    console.print("[dim]Python 3.10+. Questions? Contact via Telegram or Issues.[/]")
    console.print()
