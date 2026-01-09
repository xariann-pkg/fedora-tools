#!/usr/bin/env bash
set -euo pipefail

# Check for updates (quiet)
if dnf check-update --refresh >/dev/null 2>&1; then
    # 0 = no updates
    exit 0
fi

rc=$?
if [ "$rc" -eq 100 ]; then
    # 100 = updates available
    notify-send -u normal -i fedora-logo-icon \
        "Fedora updates available" \
        "Click the tray icon to run Fedora Update."
elif [ "$rc" -eq 1 ]; then
    # 1 = error
    notify-send -u low -i dialog-warning \
        "Fedora update check failed" \
        "dnf check-update exited with 1 (repo or network error)."
fi
