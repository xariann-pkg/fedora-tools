Name:           boot-windows
Version:        1.1
Release:        %autorelease
Summary:        Reboot into Windows via UEFI BootNext

License:        GPL-3.0-or-later
URL:            https://example.invalid/boot-windows
Source0:        boot-windows.sh
Source1:        boot-windows.desktop

BuildArch:      noarch
Requires:       efibootmgr zenity systemd desktop-file-utils libnotify

%description
Small helper to reboot into the Windows Boot Manager entry using UEFI BootNext.

%prep
# nothing to do

%build
# nothing to build

%install
rm -rf %{buildroot}

# Script -> /usr/bin/boot-windows
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/boot-windows

# Desktop file -> /usr/share/applications/boot-windows.desktop
install -D -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/applications/boot-windows.desktop

# Validate desktop file (non-fatal)
desktop-file-validate %{buildroot}%{_datadir}/applications/boot-windows.desktop || :

%files
%{_bindir}/boot-windows
%{_datadir}/applications/boot-windows.desktop

%changelog
%autochangelog

