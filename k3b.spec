# _without_reqs	- dont force optional requires

Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.9
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{version}.tar.gz
# Source0-md5:	cac0c1e80862070e9b0da2ead5ff4521
Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-0.9.tar.gz
# Source1-md5:	f4f42ad93802b0b72d92b81c80df4cca
Patch0:		%{name}-defaults.patch
Patch1:         %{name}-linux_2_5.patch
URL:		http://k3b.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-kde-devel
BuildRequires:	arts-qt
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libart_lgpl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires: 	qt-devel >= 3.0.3
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
##BuildRequires:	nas-devel
Requires:	qt >= 3.0.3
BuildRequires:	cdrdao
Requires:	cdrecord
Requires:	mkisofs 
Requires:	cdrdao >= 1.1.5
%{!?_without_reqs:Requires:	transcode >= 0.6.0}
%{!?_without_reqs:Requires:	vcdimager >= 0.7}
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

%prep
%setup -q -a1
%patch0 -p1
#%patch1 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#mkdir linux
#sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
#/usr/include/linux/cdrom.h > linux/cdrom.h


%configure \
	--disable-rpath \
	--%{!?debug:dis}%{?debug:en}able-debug 

%{__make}

cd k3b-i18n-0.9

make -f admin/Makefile.common

%configure

%{__make}

cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd k3b-i18n-0.9

%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd ..

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Utilities/CD-RW
#mv $ALD/{Applications/*,Utilities/CD-RW} 
mv $ALD/{Multimedia/*,Utilities/CD-RW} 

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_applnkdir}/Utilities/CD-RW/*
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/k3b
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/[!l]*/*/*/*
