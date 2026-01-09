#!/bin/bash
set -e

echo "== Fedora update helper =="
echo

echo "Running: sudo dnf upgrade --refresh"
echo
# Allow upgrade to fail (e.g. nothing to do, transient errors) without aborting the script
if ! sudo dnf upgrade --refresh; then
    echo
    echo "dnf upgrade exited with a non-zero status (possibly nothing to do)."
fi

echo
echo "Upgrade finished (or nothing to do)."
echo

echo "Running: sudo dnf autoremove"
if ! sudo dnf autoremove; then
    echo "Nothing to autoremove or command failed."
fi
echo

echo "Running: sudo dnf clean packages"
if ! sudo dnf clean packages; then
    echo "dnf clean packages failed (cache may already be clean)."
fi
echo

echo "All done."
echo
read -rp "Press Enter to exit..."

