# _without_reqs	- dont force optional requires

Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.8.1
Release:	2
License:	GPL
Group:		X11/Applications
# Source0-md5: 4f205fcb7afb11d8db07cac20e431819
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{version}.tar.gz
# Source1-md5: 1d1a074c61e5b9e790f3125534cae60b
Source1:	http://dl.sourceforge.net/k3b/%{name}-0.8-i18n.tar.gz
Patch0:		%{name}-defaults.patch
Patch1:         %{name}-linux_2_5.patch
URL:		http://k3b.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-kde-devel
BuildRequires:	arts-qt
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libvorbis-devel
BuildRequires: 	qt-devel >= 3.0.3
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	mad-devel
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
W�asno�ci Kreatora CD:
 - najbardziej przyjazny dla u�ytkownika interfejs ;-)
 - zapisywanie p�yt CD-Audio
 - zapisywanie p�yt ISO
 - zapisywanie istniej�cych obraz�w ISO na CD
 - kopiowanie CD (data/audio/mixed - z danymi, d�wi�kiem i mieszane)
 - czyszczenie p�yt CD-RW
 - rippowanie CD do plik�w WAV
 - rippowanie DVD przy u�yciu narz�dzi transcode
 - kodowanie DivX/XviD
 - sprawdzanie, czy u�ytkownik w�o�y� czyst� p�yt�
 - odtwarzania CD-info i TOC
 - obs�uga nagrywarek ATAPI bez emulacji SCSI przy odczycie
 - zintegrowany odtwarzacz p�yt audio o pe�nych mo�liwo�ciach.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

mkdir linux
sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
/usr/include/linux/cdrom.h > linux/cdrom.h


%configure \
	--disable-rpath \
	--%{!?debug:dis}%{?debug:en}able-debug 

%{__make}

cd k3b-0.8-i18n

%configure

%{__make}

cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd k3b-0.8-i18n

%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd ..

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Utilities/CD-RW
#mv $ALD/{Applications/*,Utilities/CD-RW} 
mv $ALD/{Multimedia/*,Utilities/CD-RW} 

%find_lang %{name} --with-kde
%find_lang k3bsetup --with-kde

cat k3bsetup.lang >>%{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/CD-RW/*
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/k3b
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/[!l]*/*/*/*
