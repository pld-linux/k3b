Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.7.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/k3b/%{name}-%{version}.tar.gz
URL:		http://k3b.sourceforge.net
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	arts-kde-devel
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libvorbis-devel
BuildRequires:	nas-devel
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	zlib-devel
Requires:	cdrecord
Requires:	mkisofs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
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
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure --enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Utilities/CD-RW
mv $ALD/{Applications/*,Utilities/CD-RW} 
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
%{_pixmapsdir}/*/*/*/*
