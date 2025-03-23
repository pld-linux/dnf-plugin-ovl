Summary:	DNF plugin to work around overlayfs issues
Name:		dnf-plugin-ovl
Version:	0.0.3
Release:	3
License:	GPL v2+
Source0:	https://github.com/FlorianLudwig/dnf-plugin-ovl/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	16b6b5f13731e39ec08493e0b2f7ba70
URL:		https://github.com/FlorianLudwig/dnf-plugin-ovl
BuildRequires:	python3-modules
Requires:	dnf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Workaround to run dnf on overlayfs. A port of yum-plugin-ovl to dnf.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/dnf-plugins

cp -p ovl.py $RPM_BUILD_ROOT%{py3_sitescriptdir}/dnf-plugins/ovl.py

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}/dnf-plugins
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}/dnf-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/dnf-plugins/ovl.py
%{py3_sitescriptdir}/dnf-plugins/__pycache__/ovl.*
