#!/usr/bin/env bash

set -euo pipefail

# Find the Windows Boot Manager entry
boot_number="$(
  efibootmgr | awk '/Windows Boot Manager/ {
    sub("^Boot","",$1); sub("\\*","",$1); print $1; exit
  }'
)"

if [ -z "${boot_number:-}" ]; then
  notify-send "Boot Windows" "Cannot find Windows boot in EFI, exiting"
  exit 1
fi

# Ask for confirmation (GUI dialog)
if ! zenity --question --title="Boot Windows" \
  --text="Reboot into Windows (Boot${boot_number}) now?"; then
  exit 0
fi

# Set next boot to Windows and reboot (GUI auth via pkexec)
pkexec efibootmgr -n "${boot_number}" && systemctl reboot
