%define debug_package %{nil}

Summary:        A tool to extract ace archives
Name:           unace
Version:        2.50
Release:        2%{?dist}
License:        Redistributable, no modification permitted
Group:          Applications/Archiving
URL:            http://www.winace.com/
Source0:        http://www.winace.com/files/linunace25.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:  i386

%description
unace is a command line utility to extract, view, and test the
contents of an ACE archive.


%prep
%setup -q -c
sed -i 's/\r//g' licence
chmod -x licence


%build
# nothing to build, upstream distributes prebuild binaries only


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
install -m 0755 %{name} $RPM_BUILD_ROOT/%{_bindir}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc licence
%{_bindir}/%{name}


%changelog
* Wed Oct 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.50-2
- Stop generation of useless debuginfo package (livna 994)
- Include licence text in documentation

* Sat Apr  8 2006 Dams <anvil[AT]livna.org> - 2.50-1
- Updated to 2.50

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun May 18 2003 Dams <anvil[AT]livna.org> 0:2.20-0.fdr.3
- License is now Distributable

* Wed May 14 2003 Dams <anvil[AT]livna.org> 0:2.20-0.fdr.2
- Added ExclusiveArch tag

* Tue May 13 2003 Dams <anvil[AT]livna.org> 
- Initial build.
