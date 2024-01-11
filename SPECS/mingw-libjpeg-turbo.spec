%?mingw_package_header

# Build the programs like cjpeg, etc.
# https://bugzilla.redhat.com/show_bug.cgi?id=467401#c7
%global build_programs 0

Name:           mingw-libjpeg-turbo
Version:        1.5.1
Release:        5%{?dist}
Summary:        MinGW Windows Libjpeg-turbo library

License:        wxWidgets
URL:            http://libjpeg-turbo.virtualgl.org/
Source0:        http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz

# Make jconfig.h more autoconf friendly
# https://bugzilla.redhat.com/show_bug.cgi?id=843193
Patch0:         libjpeg-turbo-match-autoconf-behavior.patch

BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  nasm
BuildRequires:  cmake

%description
MinGW Windows cross compiled Libjpeg-turbo library.


# Win32
%package -n mingw32-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      mingw32-libjpeg < 7-4
Provides:       mingw32-libjpeg = 7-4

%description -n mingw32-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.

%package -n mingw32-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       mingw32-libjpeg-turbo = %{version}-%{release}
Obsoletes:      mingw32-libjpeg-static < 7-4
Provides:       mingw32-libjpeg-static = 7-4

%description -n mingw32-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.

# Win64
%package -n mingw64-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      mingw64-libjpeg < 8a-2%{?dist}
Provides:       mingw64-libjpeg = 8a-2%{?dist}

%description -n mingw64-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.

%package -n mingw64-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       mingw64-libjpeg-turbo = %{version}-%{release}
Obsoletes:      mingw64-libjpeg-static < 8a-2%{?dist}
Provides:       mingw64-libjpeg-static = 8a-2%{?dist}

%description -n mingw64-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.


%?mingw_debug_package


%prep
%setup -q -n libjpeg-turbo-%{version}
%patch0 -p1


%build
%mingw_cmake
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Remove manual pages which duplicate Fedora native.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# The CMake build system also installed some docs
rm -rf $RPM_BUILD_ROOT%{mingw32_prefix}/doc
rm -rf $RPM_BUILD_ROOT%{mingw64_prefix}/doc

# Remove win32 native binaries if wanted
%if %build_programs == 0
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/*.exe
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/*.exe
%endif

# Fix perms
chmod -x README.md


# Win32
%files -n mingw32-libjpeg-turbo
%license LICENSE.md
%doc README.* ChangeLog.md
%if %build_programs
%{mingw32_bindir}/*.exe
%endif
%{mingw32_bindir}/libjpeg-62.dll
%{mingw32_bindir}/libturbojpeg.dll
%{mingw32_includedir}/jconfig.h
%{mingw32_includedir}/jerror.h
%{mingw32_includedir}/jmorecfg.h
%{mingw32_includedir}/jpeglib.h
%{mingw32_includedir}/turbojpeg.h
%{mingw32_libdir}/libjpeg.dll.a
%{mingw32_libdir}/libturbojpeg.dll.a

%files -n mingw32-libjpeg-turbo-static
%{mingw32_libdir}/libjpeg.a
%{mingw32_libdir}/libturbojpeg.a

# Win64
%files -n mingw64-libjpeg-turbo
%license LICENSE.md
%doc README.* ChangeLog.md
%if %build_programs
%{mingw64_bindir}/*.exe
%endif
%{mingw64_bindir}/libjpeg-62.dll
%{mingw64_bindir}/libturbojpeg.dll
%{mingw64_includedir}/jconfig.h
%{mingw64_includedir}/jerror.h
%{mingw64_includedir}/jmorecfg.h
%{mingw64_includedir}/jpeglib.h
%{mingw64_includedir}/turbojpeg.h
%{mingw64_libdir}/libjpeg.dll.a
%{mingw64_libdir}/libturbojpeg.dll.a

%files -n mingw64-libjpeg-turbo-static
%{mingw64_libdir}/libjpeg.a
%{mingw64_libdir}/libturbojpeg.a


%changelog
* Tue Aug 14 2018 Victor Toso <victortoso@redhat.com> - 1.5.1-5
- ExclusiveArch: i686, x86_64
- Related: rhbz#1615874

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Kalev Lember <klember@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 1.5.0-1
- Update to 1.5.0
- Include license files
- Don't set group tags

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-4
- Fix CVE-2014-9092 (RHBZ #1169851 #1169853)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-2
- Fix compatibility with older CMake versions (as used on RHEL7)

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1
- Fixes CVE-2013-6629 and CVE-2013-6630 (RHBZ #1031740)

* Sat Aug  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- Make jconfig.h more autoconf friendly (RHBZ #843193)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.90-1
- Update to 1.2.90

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Nicola Fontana <ntd@entidi.it> - 1.2.1-2
- Dropped phantom dependency on libpng and zlib (RHBZ #866185)

* Sun Oct 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.2.1-1
- Update to 1.2.1
- Dropped upstreamed int32 patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-8
- Added win64 support
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-7
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-5
- Updated the INT32 patch so that both the mingw.org and the mingw-w64
  toolchains are supported

* Fri Jun  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-4
- Fix a conflict between w32api's basetsd.h and jmorecfg.h (conflicting
  declarations for INT32)

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-3
- Moved the obsoletes/provides to the right location
- Bundle the licence and other %%doc's
- Fixed a small rpmlint warning

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-2
- Use CMake to build this package as it creates a more mingw-friendly
  version of the library

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1
- Temporary made the package compliant to the old guidelines as the new
  mingw-w64 based toolchain isn't approved for inclusion in Fedora yet

* Fri Apr 15 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Made the package compliant with the new approved packaging guidelines

* Tue Feb 15 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1-3
- Bumped the obsoletes mingw32-libjpeg

* Wed Jan 19 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1-2
- Generate per-target RPMs

* Sun Oct  3 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1-1
- Initial release (based on mingw32-libjpeg)
- Dropped the BR: mingw32-dlfcn
- Obsoletes/provides mingw32-libjpeg and mingw32-libjpeg-static
- Disable SIMD support for now because libtool doesn't recognize nasm

