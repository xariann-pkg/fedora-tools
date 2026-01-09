Name:           fedora-update
Version:        1.1
Release:        %autorelease
Summary:        Interactive DNF update and cleanup helper

License:        GPL-3.0-or-later
URL:            https://github.com/xariann-pkg/fedora-tools
Source0:        fedora-update.sh
Source1:        fedora-update.desktop
Source2:        fedora-update-tray.py
Source3:        fedora-update-tray.desktop
Source4:        fedora-update-tray.service
Source5:        fedora-updates.png
Source6:        fedora-update-check
Source7:        fedora-update-check.service
Source8:        fedora-update-check.timer

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

Requires:       dnf
Requires:       python3
Requires:       python3-pystray
Requires:       python3-pillow

%description
Interactive helper that checks for updates, runs dnf upgrade, autoremove
and cache cleanup, accessible from the desktop menu, plus an optional
tray helper that periodically checks for updates. [cite: 10, 12]

%prep
%autosetup -c -T

%build

%install
rm -rf %{buildroot}

install -D -m 0755 %{_sourcedir}/fedora-update.sh %{buildroot}%{_bindir}/fedora-update
install -D -m 0644 %{_sourcedir}/fedora-update.desktop %{buildroot}%{_datadir}/applications/fedora-update.desktop
install -D -m 0755 %{_sourcedir}/fedora-update-tray.py %{buildroot}%{_bindir}/fedora-update-tray
install -D -m 0644 %{_sourcedir}/fedora-update-tray.desktop %{buildroot}%{_datadir}/applications/fedora-update-tray.desktop
install -D -m 0644 %{_sourcedir}/fedora-update-tray.service %{buildroot}%{_userunitdir}/fedora-update-tray.service
install -D -m 0644 %{_sourcedir}/fedora-updates.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/fedora-updates.png
install -D -m 0755 %{_sourcedir}/fedora-update-check %{buildroot}%{_bindir}/fedora-update-check
install -D -m 0644 %{_sourcedir}/fedora-update-check.service %{buildroot}%{_userunitdir}/fedora-update-check.service
install -D -m 0644 %{_sourcedir}/fedora-update-check.timer %{buildroot}%{_userunitdir}/fedora-update-check.timer

%files
%{_bindir}/fedora-update
%{_datadir}/applications/fedora-update.desktop
%{_bindir}/fedora-update-tray
%{_datadir}/applications/fedora-update-tray.desktop
%{_bindir}/fedora-update-check
%{_userunitdir}/fedora-update-tray.service
%{_userunitdir}/fedora-update-check.service
%{_userunitdir}/fedora-update-check.timer
%{_datadir}/icons/hicolor/32x32/apps/fedora-updates.png

%changelog
%autochangelog
