%global debug_package %{nil}
%global __strip /bin/true

Summary:        A tool to extract ace archives
Name:           unace
Version:        2.50
Release:        18%{?dist}
License:        Redistributable, no modification permitted
Group:          Applications/Archiving
URL:            http://www.winace.com/
Source0:        http://www.winace.com/files/linunace25.tgz
ExclusiveArch:  i686

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
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 %{name} %{buildroot}%{_bindir}/


%files
%license licence
%{_bindir}/%{name}


%changelog
* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.50-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.50-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.50-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.50-15
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 2.50-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.50-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.50-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.50-11
- Package clean-up

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.50-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.50-8
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Fix default arch for the binary package

* Sun Mar 29 2009 Julian Sikorski <belegdol@fedoraproject.org> - 2.50-6
- Fedora 11 is i586, not i386

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.50-5
- rebuild for new F11 features

* Sun Aug 10 2008 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.50-4
- add a delay during build for now to fool RPM Fusion's buildsys

* Fri Jul 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.50-3
- Release bump for rpmfusion

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
