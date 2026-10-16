# -*- coding: utf-8 -*-
"""Tonkeeper Fake Balance — Rich terminal UI"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console(force_terminal=True, color_system="auto")

LOGO = r"""████████╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗███████╗██████╗ ███████╗██████╗
╚══██╔══╝██╔═══██╗████╗  ██║██║ ██╔╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
   ██║   ██║   ██║██╔██╗ ██║█████╔╝ █████╗  █████╗  ██████╔╝█████╗  ██████╔╝
   ██║   ██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║ ╚████║██║  ██╗███████╗███████╗██║     ███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
      ███████╗ █████╗ ██╗  ██╗███████╗
      ██╔════╝██╔══██╗██║ ██╔╝██╔════╝
      █████╗  ███████║█████╔╝ █████╗
      ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝
      ██║     ██║  ██║██║  ██╗███████╗
      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝"""


def print_banner():
    panel = Panel(
        Text.from_markup(
            f"[bold cyan]{LOGO}[/]\n\n"
            "[bold white]T O N   W A L L E T   O V E R L A Y[/]\n"
            "[dim]Tonkeeper  |  TON + Jettons  |  Persistent Hooks  |  Screenshot-Safe[/]"
        ),
        box=box.ROUNDED, border_style="cyan", padding=(0, 2),
        title="[bold white on cyan] TONKEEPER FAKE BALANCE [/]", title_align="center",
    )
    console.print(panel)


def show_menu_table(menu_items: list) -> str:
    console.print()
    console.print(Rule("[bold cyan]MENU[/]", style="cyan"))
    table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE, expand=True)
    table.add_column("[#]", style="bold", justify="center", width=4)
    table.add_column("Action", style="green")
    table.add_column("Description", style="dim")
    for key, action, desc in menu_items:
        table.add_row(key, action, desc)
    console.print(table)
    return console.input("\n[bold cyan]Select action [#]: [/]").strip()


def show_load_status_table(config: dict):
    console.print()
    console.print(Rule("[bold cyan]STATUS[/]", style="cyan"))
    table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE)
    table.add_column("Parameter", style="green")
    table.add_column("Value", justify="center")
    table.add_column("Status", justify="center", style="bold")
    tk_path = config.get("tonkeeper_path", "auto")
    balances = config.get("target_balances", {})
    table.add_row("Tonkeeper Path", str(tk_path), "[green]AUTO[/]" if tk_path == "auto" else "[cyan]CUSTOM[/]")
    table.add_row("Target Assets", str(len(balances)), "[green]OK[/]" if balances else "[red]NONE[/]")
    table.add_row("Hook Mode", config.get("hook_mode", "memory"), "[green]READY[/]")
    table.add_row("Persistence", "ON" if config.get("persist_on_restart") else "OFF", "[green]OK[/]" if config.get("persist_on_restart") else "[dim]-[/]")
    console.print(table)
    console.print()


def show_balance_table(balances: list):
    console.print()
    console.print(Rule("[bold cyan]TARGET BALANCES[/]", style="cyan"))
    table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE)
    table.add_column("#", style="dim", justify="right", width=3)
    table.add_column("Asset", style="cyan")
    table.add_column("Amount", style="green", justify="right")
    table.add_column("USD Value", style="yellow", justify="right")
    for i, row in enumerate(balances):
        table.add_row(str(i + 1), *row)
    console.print(table)
    console.print()


def show_hook_status_table(status_rows: list):
    console.print()
    console.print(Rule("[bold cyan]HOOK STATUS[/]", style="cyan"))
    table = Table(show_header=True, header_style="bold cyan", border_style="dim", box=box.SIMPLE)
    table.add_column("Component", style="green")
    table.add_column("PID", justify="center", style="cyan")
    table.add_column("State", justify="center")
    for row in status_rows:
        table.add_row(*row)
    console.print(table)
    console.print()


def print_success(msg: str):
    console.print(f"[green]+[/] {msg}")


def print_error(msg: str):
    console.print(f"[red]x[/] {msg}")


def print_info(msg: str):
    console.print(f"[cyan]i[/] {msg}")


def print_warning(msg: str):
    console.print(f"[yellow]![/] {msg}")


def progress_bar(current: int, total: int, width: int = 30, prefix: str = ""):
    filled = int(width * current / total) if total > 0 else 0
    pct = (current / total * 100) if total > 0 else 0
    bar = "#" * filled + "." * (width - filled)
    console.print(f"\r{prefix}[cyan]{bar}[/] [dim]{pct:.0f}%[/]", end="")
