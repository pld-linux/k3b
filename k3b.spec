#
# TODO:
# - some dirs are from packages they aren't in R (vide konqueror dir)
# - nas support is obsolete? it depends on kdelibs build type
# - cosmetics in build and install sections
# - is this bcond is really needed? lack of features makes users angry
# - bcond for alsa: what if arts was compiled with alsa?
#
# Conditional build:
%bcond_without reqs		# don't force optional Requires
#
Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/k3b/%{name}-%{version}.tar.gz
# Source0-md5:	480b6d6777a9151868677a1ae078e7c7
Source1:	http://dl.sourceforge.net/sourceforge/k3b/%{name}-i18n-%{version}.tar.gz
# Source1-md5:	a14fd760bb146eaee22802c504e53152
URL:		http://k3b.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-kde-devel
BuildRequires:	arts-qt
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	zlib-devel
##BuildRequires:	nas-devel
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

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libk3bcore.

%prep
%setup -q -a1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

# same thing as with kdemultimedia
# includes kernel headers which breaks things
# with PLD kernels 2.4.x, below workaround  by misiek

mkdir linux scsi
sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
/usr/include/linux/cdrom.h > linux/cdrom.h
cp /usr/include/scsi/scsi.h scsi

%configure \
	--disable-rpath \
	--%{!?debug:dis}%{?debug:en}able-debug
%{__make}

cd %{name}-i18n-%{version}
	make -f admin/Makefile.common
	%configure
	%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd %{name}-i18n-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Utilities/CD-RW
#mv $ALD/{Applications/*,Utilities/CD-RW}
mv $ALD/{Multimedia/*,Utilities/CD-RW}
mv $ALD/{Settings/System/*,Utilities/CD-RW}
mv $ALD/.hidden/* $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_applnkdir}/Utilities/CD-RW/*
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/k3b
%{_datadir}/mimelnk/application/*
%{_datadir}/sounds/*.wav
%{_pixmapsdir}/[!l]*/*/*/*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
