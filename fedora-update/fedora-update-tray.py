#!/usr/bin/env python3

import subprocess
import sys

import pystray
from pystray import MenuItem as Item
from PIL import Image

FEDORA_ICON_OK = "/usr/share/icons/hicolor/32x32/apps/fedora-logo-icon.png"

# Use xdg-terminal-exec to remain terminal-agnostic
TERMINAL_CMD = ["xdg-terminal-exec"]


def run_fedora_update():
    # Use absolute path to ensure the script is found
    cmd = TERMINAL_CMD + ["/usr/bin/fedora-update"]
    subprocess.Popen(cmd)


def load_icon(path):
    return Image.open(path)


class UpdateTray:
    def __init__(self):
        self.icon_ok = load_icon(FEDORA_ICON_OK)

        self.icon = pystray.Icon(
            "fedora-update",
            icon=self.icon_ok,
            title="Fedora Update",
            menu=pystray.Menu(
                Item("Run updates", lambda _: run_fedora_update()),
                Item("Quit", self.quit),
            ),
        )

    def quit(self, _):
        self.icon.stop()

    def run(self):
        self.icon.run()


def main():
    try:
        UpdateTray().run()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
