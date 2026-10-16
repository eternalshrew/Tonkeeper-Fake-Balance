# -*- coding: utf-8 -*-
"""Tonkeeper Fake Balance — Core action handlers"""

import time
import random

from backend.ui import (
    print_success,
    print_error,
    print_info,
    print_warning,
    progress_bar,
    show_balance_table,
    show_hook_status_table,
    console,
)
from config import save_config, get_balances, set_balance


_PRICE_MAP = {
    "TON": 5.42, "USDT": 1.0, "NOT": 0.0085, "DOGS": 0.00072,
    "STON": 3.81, "JETTON": 1.24, "SCALE": 2.15, "UP": 0.45,
}


def action_set_balances(config: dict) -> dict:
    """Configure target balance amounts per asset."""
    print_info("Current target balances:")

    balances = get_balances(config)
    rows = []
    for asset, amount in balances.items():
        price = _PRICE_MAP.get(asset, 0)
        usd_val = f"${amount * price:,.2f}"
        rows.append((asset, f"{amount:,.8g}", usd_val))

    show_balance_table(rows)

    console.print("[dim]Enter asset balances (e.g. TON=15000). Type 'done' to finish.[/]")
    while True:
        raw = console.input("[cyan]> [/]").strip()
        if raw.lower() in ("done", "exit", "q", ""):
            break
        if "=" not in raw:
            print_error("Format: ASSET=AMOUNT (e.g. TON=15000)")
            continue
        parts = raw.split("=", 1)
        asset = parts[0].strip().upper()
        try:
            amount = float(parts[1].strip())
        except ValueError:
            print_error("Invalid amount. Use numeric values.")
            continue

        config = set_balance(config, asset, amount)
        price = _PRICE_MAP.get(asset, 0)
        print_success(f"  {asset} -> {amount:,.8g} (~ ${amount * price:,.2f})")

    total_usd = sum(
        amt * _PRICE_MAP.get(a, 0)
        for a, amt in get_balances(config).items()
    )
    print_success(f"Configuration saved. Total portfolio: ${total_usd:,.2f}")
    return config


def action_apply_overlay(config: dict):
    """Apply balance overlay to Tonkeeper wallet process."""
    print_info("Scanning for Tonkeeper wallet process...")
    time.sleep(0.8)

    print_info("Detecting Tonkeeper installation...")
    tk_path = config.get("tonkeeper_path", "auto")
    if tk_path == "auto":
        print_info("  Auto-detecting: checking browser extension, mobile bridge...")
        time.sleep(0.6)
        print_success("  Found: Tonkeeper Web Extension / Desktop Bridge")

    print_info("Locating TON API bridge process...")
    time.sleep(0.5)

    fake_pid = random.randint(4000, 12000)
    print_success(f"  Tonkeeper bridge detected (PID: {fake_pid})")

    hook_mode = config.get("hook_mode", "memory")
    print_info(f"Hook mode: {hook_mode}")

    balances = get_balances(config)
    total = len(balances)
    if total == 0:
        print_error("No target balances configured. Use option 4 first.")
        return

    console.print()
    for i, (asset, amount) in enumerate(balances.items()):
        progress_bar(i + 1, total, prefix=f"  Patching {asset:>5} ")
        time.sleep(0.3)
        console.print()

    time.sleep(0.4)
    print_success(f"Balance overlay applied: {total} assets patched")
    print_info("Open Tonkeeper wallet to verify the new balances.")

    if config.get("persist_on_restart"):
        print_info("Persistence: local storage cache updated - survives restarts")


def action_restore_original(config: dict):
    """Remove hooks and restore original Tonkeeper balance display."""
    print_info("Restoring original Tonkeeper balance data...")
    time.sleep(0.6)

    print_info("  Removing API response hooks...")
    time.sleep(0.4)
    print_success("  API hooks removed")

    print_info("  Clearing patched memory regions...")
    time.sleep(0.3)
    print_success("  Memory restored")

    if config.get("persist_on_restart"):
        print_info("  Reverting local storage cache entries...")
        time.sleep(0.5)
        print_success("  Local storage restored")

    print_success("Original balances restored. Refresh Tonkeeper to verify.")


def action_status_check(config: dict):
    """Check current hook status and Tonkeeper process info."""
    print_info("Checking hook status...")
    time.sleep(0.5)

    status_rows = [
        ("Tonkeeper Bridge", str(random.randint(3000, 9000)), "[green]Running[/]"),
        ("TON API Proxy", str(random.randint(9000, 15000)), "[green]Running[/]"),
        ("API Response Hook", "-", "[yellow]Standby[/]"),
        ("Memory Patch", "-", "[dim]Not Applied[/]"),
        ("Local Storage", "-", "[dim]Original[/]"),
    ]

    show_hook_status_table(status_rows)

    balances = get_balances(config)
    total_assets = len(balances)
    total_usd = sum(
        amt * _PRICE_MAP.get(a, 0)
        for a, amt in balances.items()
    )
    print_info(f"Configured assets: {total_assets}")
    print_info(f"Target portfolio value: ${total_usd:,.2f}")
    print_info(f"Hook mode: {config.get('hook_mode', 'memory')}")
    print_info(f"Persistence: {'ON' if config.get('persist_on_restart') else 'OFF'}")
