#
# TODO & NOTES:
# - subpackages (to kill stupid reqs bcond)
# - it overrides rpm*flags (hardcoded -O2)
#
# Conditional build:
%bcond_with	reqs		# force optional Requires
%bcond_without	setup		# don't build K3bSetup2 KControl Module
%bcond_with	linux22		# building on kernel 2.2.x
#
%define		_i18nver	0.11
Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.11.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://unc.dl.sourceforge.net/k3b/%{name}-%{version}.tar.bz2
# Source0-md5:	0015b9ad457713425464dbdad6a15ab9
Source1:	http://unc.dl.sourceforge.net/k3b/%{name}-i18n-%{_i18nver}.tar.bz2
# Source1-md5:	43b17b012ebb33cd9582742bf16064a5
Patch0:		%{name}-linux22.patch
Patch1:		%{name}-desktop.patch
URL:		http://k3b.sourceforge.net/
BuildRequires:	arts-qt-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	xrender-devel
Requires:	cdrdao >= 1.1.5
Requires:	cdrecord
Requires:	mkisofs
Requires:	qt >= 3.1
%if %{with reqs}
Requires:	transcode >= 0.6.0
Requires:	vcdimager >= 0.7
Requires:	normalize
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CD Kreator features:
 - the most userfriendly interface ever ;-)
 - writing audio-cds
 - writing ISO-cds
 - writing existing iso-images to cd
 - cd copy (data, audio, mixed mode)
 - blanking of cdrws
 - cd ripping to wav
 - dvd ripping with the transcode tools
 - DivX/XviD encoding
 - K3b checks if the user inserted an empty disk
 - Retrieving cd info and toc
 - Support for ATAPI drives without SCSI-emulation for reading
 - integrated full featured audio player

%description -l pl
W³asno¶ci Kreatora CD:
 - najbardziej przyjazny dla u¿ytkownika interfejs ;-)
 - zapisywanie p³yt CD-Audio
 - zapisywanie p³yt ISO
 - zapisywanie istniej±cych obrazów ISO na CD
 - kopiowanie CD (data/audio/mixed - z danymi, d¼wiêkiem i mieszane)
 - czyszczenie p³yt CD-RW
 - rippowanie CD do plików WAV
 - rippowanie DVD przy u¿yciu narzêdzi transcode
 - kodowanie DivX/XviD
 - sprawdzanie, czy u¿ytkownik w³o¿y³ czyst± p³ytê
 - odtwarzania CD-info i TOC
 - obs³uga nagrywarek ATAPI bez emulacji SCSI przy odczycie
 - zintegrowany odtwarzacz p³yt audio o pe³nych mo¿liwo¶ciach.

%package devel
Summary:	Header files for libk3bcore library
Summary(pl):	Pliki nag³ówkowe biblioteki libk3bcore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libk3bcore.

%prep
%setup -q -a1
%{?with linux22:%patch0 -p1}
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	%{!?with_setup:--with-k3bsetup=no}
	
%{__make}

cd %{name}-i18n-%{version}
%{__make} -f admin/Makefile.common
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}/kde \
	k3bsetup2dir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}
	
%{__make} install -C %{name}-i18n-%{version} \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README FAQ ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/libk3b*.so
%{_libdir}/kde3/libk3b*.la
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%{_libdir}/libk3baudiometainforenamerplugin.la
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/k3b
%{_datadir}/mimelnk/application/x-k3b.desktop
%{_datadir}/sounds/*.wav
%{_datadir}/applnk/.hidden/*.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/apps/k3b.png

%if %{with setup}
%attr(755,root,root) %{_libdir}/kde3/kcm_*.so
%{_libdir}/kde3/kcm_*.la
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libk3bcore.so
%{_libdir}/libk3bcore.la
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%{_libdir}/libk3bdevice.la
%attr(755,root,root) %{_libdir}/libk3bplugin.so
%{_libdir}/libk3bplugin.la
%attr(755,root,root) %{_libdir}/libk3bproject.so
%{_libdir}/libk3bproject.la
%attr(755,root,root) %{_libdir}/libk3btools.so
%{_libdir}/libk3btools.la
%{_includedir}/*.h
