# Fedora Tools

A personal collection of Fedora rpms. COPR available: https://copr.fedorainfracloud.org/coprs/xariann/tools/

## Fedora Update
Emulates arch-update by updating your system, then cleans up old dependencies and cache. Once installed enable the systemd service for the system tray icon:

```bash
systemctl --user enable --now fedora-update-tray.service
```

To make sure the updates are checked every hour also enable the timer:

```bash
systemctl --user enable --now fedora-update-check.timer
```

## Boot Windows
A script that finds your Windows boot entry and then asks you if you want to reboot to Windows.

## Nautiterm
Adds an option to GNOME nautilus to open any terminal of choice with the right click contextual menu. This is based on the work of Mika Wahlroos  in this repo https://github.com/mwahlroos/Nautiterm. It is not my work, I just packaged it for Fedora.
