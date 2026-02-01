# This gets rewritten automatically by .copr/Makefile at build time
%global snapshotdate  SNAPSHOTDATE_PLACEHOLDER

Name:           declaro
Version:        0.%{snapshotdate}
Release:        %autorelease
Summary:        Declarative wrapper around your package manager

License:        MIT
URL:            https://github.com/mantinhas/declaro
Source0:        %{url}/archive/refs/heads/main.tar.gz#/declaro-main.tar.gz

BuildArch:      noarch

# Runtime dependencies (from upstream README)
Requires:       git
Requires:       bash
Requires:       diffutils
Requires:       sed
Requires:       findutils
Requires:       make
Requires:       sudo
Requires:       coreutils
Requires:       tar
Requires:       dnf

%description
Declaro is a simple yet powerful declarative wrapper for any package
manager. It lets you define a clean "reset state" for your system and
provides tools to keep your system aligned with that state.

%prep
%autosetup -n declaro-main

%build
# Shell scripts only, nothing to build

%install
install -Dm755 src/declaro.sh \
    %{buildroot}%{_bindir}/declaro

install -Dm644 src/utils.sh \
    %{buildroot}%{_datadir}/declaro/bin/utils.sh

for cmd in src/commands/*.sh; do
    install -Dm644 "$cmd" \
        %{buildroot}%{_datadir}/declaro/bin/$(basename "$cmd")
done

install -Dm644 config/*-config.sh \
    %{buildroot}%{_datadir}/declaro/config/

%post
# Create a default /etc/declaro/config.sh on first install only
if [ ! -f /etc/declaro/config.sh ]; then
    mkdir -p /etc/declaro
    if [ -f /usr/share/declaro/config/dnf-config.sh ]; then
        cp /usr/share/declaro/config/dnf-config.sh /etc/declaro/config.sh
        chmod 0644 /etc/declaro/config.sh
    fi
fi

%files
%doc README.md
%{_bindir}/declaro
%{_datadir}/declaro

%changelog
%autochangelog
