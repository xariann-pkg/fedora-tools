Name:           boot-windows
Version:        1.1
Release:        %autorelease
Summary:        Reboot into Windows via UEFI BootNext

License:        GPL-3.0-or-later
URL:            https://github.com/xariann-pkg/fedora-tools
Source0:        boot-windows.sh
Source1:        boot-windows.desktop

BuildArch:      noarch
Requires:       efibootmgr zenity systemd desktop-file-utils libnotify

%description
Small helper to reboot into the Windows Boot Manager entry using UEFI BootNext.

%prep
%autosetup -c -T

%build

%install
rm -rf %{buildroot}

install -D -m 0755 %{_sourcedir}/boot-windows.sh %{buildroot}%{_bindir}/boot-windows
install -D -m 0644 %{_sourcedir}/boot-windows.desktop %{buildroot}%{_datadir}/applications/boot-windows.desktop

%files
%{_bindir}/boot-windows
%{_datadir}/applications/boot-windows.desktop

%changelog
%autochangelog
