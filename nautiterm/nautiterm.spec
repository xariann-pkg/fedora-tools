Name:           nautiterm
Version:        1.0
Release:        1%{?dist}
Summary:        Open a terminal of your choice from Nautilus

License:        GPL-2.0-only
URL:            https://github.com/mwahlroos/Nautiterm
Source0:        https://github.com/mwahlroos/Nautiterm/archive/refs/heads/master/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       nautilus-python
Requires:       python3-pyyaml

%description
Nautilus Python extension that adds an “Open Terminal Here” menu entry
and lets you configure which terminal emulator to use.

%prep
%autosetup -n Nautiterm-master

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions
install -m 0644 src/nautiterm/open_terminal.py \
    %{buildroot}%{_datadir}/nautilus-python/extensions/open_terminal.py

%files
%{_datadir}/nautilus-python/extensions/open_terminal.py

%changelog
* Sun Jan 04 2026 You <xariann.widely103@passmail.com> - 1.0-1
- Initial package

