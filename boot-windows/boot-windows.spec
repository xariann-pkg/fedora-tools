Name:           boot-windows
Version:        1.4
Release:        %autorelease
Summary:        Reboot into Windows via UEFI BootNext

License:        GPL-3.0-or-later
URL:            https://github.com/xariann-pkg/fedora-tools
Source0:        boot-windows.sh
Source1:        boot-windows.desktop

BuildArch:      noarch
Requires:       efibootmgr 
Requires:       zenity 
Requires:       systemd
Requires:       desktop-file-utils 
Requires:       libnotify 

%description
Small helper to reboot into the Windows Boot Manager entry using UEFI BootNext. 

%prep
%autosetup -c -T
# Copy sources to the current build directory
cp %{SOURCE0} %{SOURCE1} .

%build
# No build steps needed for a shell script

%install
# Create directories
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications

# Install the script. We use 'install' to set permissions (0755)
install -p -m 0755 boot-windows.sh %{buildroot}%{_bindir}/boot-windows

# Install the desktop entry
install -p -m 0644 boot-windows.desktop %{buildroot}%{_datadir}/applications/boot-windows.desktop

%files
%{_bindir}/boot-windows
%{_datadir}/applications/boot-windows.desktop

%changelog
%autochangelog