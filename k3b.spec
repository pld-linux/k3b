Summary:	The CD Kreator
Name:		k3b
Version:	0.7.4
Release:	0
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/k3b/%{name}-%{version}.tar.gz
URL:		http://k3b.sourceforge.net
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	kdelibs-devel
BuildRequires:	libvorbis-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	arts-kde-devel
BuildRequires:	fam-devel
BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	nas-devel
BuildRequires:	gettext-devel
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

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-kde
%find_lang k3bsetup --with-kde
cat k3bsetup.lang >>%{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Applications/*
%{_applnkdir}/Multimedia/*
%{_datadir}/apps/k3b
%{_pixmapsdir}/*/*/*/*
