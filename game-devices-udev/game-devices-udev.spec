Name:           game-devices-udev
Version:        0.24
Release:        1%{?dist}
Summary:        Udev rules for game controllers
BuildArch:      noarch

License:        MIT
URL:            https://codeberg.org/fabiscafe/game-devices-udev
# Codeberg archives extract to a folder named "repo-name" usually, 
# but we can handle standard source archives or git snapshots.
# This URL assumes a git tag exists for the version. 
# If downloading a snapshot, you might need to adjust Source0.
Source0:        https://codeberg.org/fabiscafe/%{name}/archive/%{version}.tar.gz

Requires:       udev
Requires:       systemd

%description
A collection of udev rules for various game controllers to ensure they 
are recognized and configured correctly. This package also loads the 
uinput module at boot.

%prep
# -n sets the directory name the tarball extracts to. 
# Codeberg archive tarballs usually extract to a folder named "{name}" (without version)
%setup -q -n %{name}

%build
# Nothing to build, these are just text files

%install
# 1. Install Udev rules
# Package rules go into /usr/lib/udev/rules.d/ (distro path), 
# leaving /etc/udev/rules.d/ for your manual overrides.
install -d -m 0755 %{buildroot}%{_prefix}/lib/udev/rules.d
install -m 0644 *.rules %{buildroot}%{_prefix}/lib/udev/rules.d/

# 2. Create modules-load.d config
# Package module configs go into /usr/lib/modules-load.d/
install -d -m 0755 %{buildroot}%{_prefix}/lib/modules-load.d
echo "uinput" > %{buildroot}%{_prefix}/lib/modules-load.d/uinput.conf
chmod 0644 %{buildroot}%{_prefix}/lib/modules-load.d/uinput.conf

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/udev/rules.d/*.rules
%{_prefix}/lib/modules-load.d/uinput.conf

%changelog
%autochangelog