Name: hunspell-ko
Summary: Korean hunspell dictionaries
Version: 0.5.5
Release: 4%{?dist}
Source: http://spellcheck-ko.googlecode.com/files/hunspell-dict-ko-%{version}.tar.gz
Group: Applications/Text
URL: http://code.google.com/p/spellcheck-ko/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: MPLv1.1 or GPLv2 or LGPLv2
BuildArch: noarch
BuildRequires: python-lxml, hunspell
Requires: hunspell

%description
Korean hunspell dictionaries.

%prep
%setup -q -n hunspell-dict-ko-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ko.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.aff
cp -p ko.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.dic

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README LICENSE LICENSE.GPL LICENSE.LGPL LICENSE.MPL
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.5.5-1
- latest version

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.5.4-1
- latest version

* Sun May 22 2011 Caolán McNamara <caolanm@redhat.com> - 0.5.3-1
- latest version

* Mon Apr 04 2011 Caolán McNamara <caolanm@redhat.com> - 0.5.2-1
- latest version

* Mon Mar 21 2011 Caolán McNamara <caolanm@redhat.com> - 0.5.1-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Caolán McNamara <caolanm@redhat.com> - 0.5.0-1
- latest version

* Sat Aug 07 2010 Caolán McNamara <caolanm@redhat.com> - 0.4.3-1
- latest version
- drop integrated hunspell-dict-ko-0.4.2-1278333282.fixtests.patch

* Mon Jul 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.4.2-2
- enable make check now that hunspell is fixed to know about
  hangul syllables

* Mon Jul 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.4.2-1
- latest version

* Tue Jun 08 2010 Caolán McNamara <caolanm@redhat.com> - 0.4.1-1
- latest version

* Mon Mar 01 2010 Caolán McNamara <caolanm@redhat.com> - 0.4.0-1
- latest version

* Tue Nov 03 2009 Caolán McNamara <caolanm@redhat.com> - 0.3.5-1
- latest version

* Sun Aug 30 2009 Caolán McNamara <caolanm@redhat.com> - 0.3.3-1
- latest version

* Sun Jul 26 2009 Caolán McNamara <caolanm@redhat.com> - 0.3.2-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.3.1-1
- latest version

* Mon Jun 22 2009 Caolán McNamara <caolanm@redhat.com> - 0.3.0-1
- latest version

* Wed Jun 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.4-2
- build from source

* Mon Jun 15 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.4-1
- initial version
