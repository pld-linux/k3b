#
# TODO & NOTES:
# - some dirs are from packages they aren't in R (vide konqueror dir)
# - is this reqs bcond really needed?
# - it overrides rpm*flags (hardcoded -O2)
#
# Conditional build:
%bcond_without	reqs		# don't force optional Requires
%bcond_without	setup		# don't build K3bSetup2 KControl Module
%bcond_with	linux22		# building on kernel 2.2.x
#

# 0.11 not ready yet, waits for KDE 3.2
%define		_i18nver	0.10

Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.11.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{version}.tar.bz2
# Source0-md5:	6e7ce4f85c9b2e159c6308fad5350bdf
Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-%{_i18nver}.tar.gz
# Source1-md5:	a14fd760bb146eaee22802c504e53152
Patch0:		%{name}-linux22.patch
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

%define         _htmldir        /usr/share/doc/kde/HTML

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
Requires:	%{name} = %{version}
Requires:	kdelibs-devel

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libk3bcore.

%prep
%setup -q -a1
%if %{with linux22}
%patch0 -p1
%endif

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

cp -f /usr/share/automake/config.sub admin

%configure \
	--with-qt-libraries=%{_libdir} \
	%{!?with_setup:--with-k3bsetup=no} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath
	
%{__make}

#cd %{name}-i18n-%{_i18nver}
#%%{__make} -f admin/Makefile.common
#%%configure
#%%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%{__make} install -C %{name}-i18n-%{_i18nver} \
#	DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Utilities/CD-RW
#mv $ALD/{Applications/*,Utilities/CD-RW}
mv $ALD/{Multimedia/*,Utilities/CD-RW}
%{?with_setup:mv $ALD/{Settings/System/*,Utilities/CD-RW}}
mv $ALD/.hidden/* $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README FAQ ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/libk3b*.so
%{_libdir}/kde3/libk3b*.la
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%{_libdir}/libk3baudiometainforenamerplugin.la
%{_applnkdir}/Utilities/CD-RW/*
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/k3b
%{_datadir}/mimelnk/application/*
%{_datadir}/sounds/*.wav
%{_pixmapsdir}/[!l]*/*/*/*
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
