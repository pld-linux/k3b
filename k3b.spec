#
# Conditional build:
%bcond_with	linux22		# building on kernel 2.2.x

%define		_ver		0.11.90
%define		_i18nver	0.11
%define		_snap		040516

Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	%{_ver}.%{_snap}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-%{_i18nver}.tar.bz2
# Source1-md5:	80d1ac1766ad8a8cdadca5f4273f2d95
Patch0:		%{name}-linux22.patch
Patch1:		%{name}-desktop.patch
URL:		http://k3b.sourceforge.net/
BuildRequires:	arts-qt-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	cdparanoia-III-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	kdelibs-devel >= 3.2.90
BuildRequires:	lame-libs-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
#BuildRequires:	unsermake >= 040511
Requires:	cdrecord
Requires:	kdebase-core >= 3.2.90
Requires:	mkisofs
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

%package devel
Summary:	Header files for libk3bcore library
Summary(pl):	Pliki nag��wkowe biblioteki libk3bcore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag��wkowe biblioteki libk3bcore.

%package plugin-decoder-flac
Summary:	Decoder plugin - flac
Summary(pl):	Wtyczka dekoduj�ca - flac
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-flac
Decoding module to decode FLAC files.
 
%description plugin-decoder-flac -l pl
Modu� dekodujacy pliki w formacie FLAC.

%package plugin-decoder-mad
Summary:	Decoder plugin - mad
Summary(pl):	Wtyczka dekoduj�ca - mad
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-mad
Decoding module to decode MPEG 1 Layer III files.
 
%description plugin-decoder-mad -l pl
Modu� dekodujacy pliki w formacie MPEG 1 Layer III.

%package plugin-decoder-oggvorbis
Summary:	Decoder plugin - oggvorbis
Summary(pl):	Wtyczka dekoduj�ca - oggvorbis
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-oggvorbis
Decoding module to decode Ogg Vorbis files.
 
%description plugin-decoder-oggvorbis -l pl
Modu� dekodujacy pliki w formacie Ogg Vorbis.

%package plugin-decoder-wave
Summary:	Decoder plugin - wave
Summary(pl):	Wtyczka dekoduj�ca - wave
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-wave
Decoding module to decode wave files.
 
%description plugin-decoder-wave -l pl
Modu� dekodujacy pliki w formacie wave.

%package plugin-encoder-external
Summary:	Encoder plugin - external
Summary(pl):	Wtyczka koduj�ca - external
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-encoder-external
Encoding module that allows specifying an encoding command.
 
%description plugin-encoder-external -l pl
Modu� koduj�cy pozwalaj�cy na sformu�owanie komendy kodowania.

%package plugin-encoder-lame
Summary:	Encoder plugin - lame
Summary(pl):	Wtyczka koduj�ca - lame
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-encoder-lame
Encoding module to encode MP3 files.
 
%description plugin-encoder-lame -l pl
Modu� koduj�cy pliki w formacie MP3.

%package plugin-encoder-oggvorbis
Summary:	Encoder plugin - oggvorbis
Summary(pl):	Wtyczka koduj�ca - oggvorbis
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-encoder-oggvorbis
Encoding module to encode Ogg Vorbis files.
 
%description plugin-encoder-oggvorbis -l pl
Modu� koduj�cy pliki w formacie Ogg Vorbis.

%package plugin-encoder-sox
Summary:	Encoder plugin - sox
Summary(pl):	Wtyczka koduj�ca - sox
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	sox

%description plugin-encoder-sox
Encoding module to encode many file formats using sox.
 
%description plugin-encoder-sox -l pl
Modu� koduj�cy pliki w wielu formatach u�ywaj�c programu sox.

%prep
%setup -q -n %{name}-%{_snap} -a1
%{?with_linux22:%patch0 -p1}
%patch1 -p1

%build

cp -f /usr/share/automake/config.sub admin
cp -f /usr/share/automake/config.sub k3b-i18n-%{_i18nver}/admin

#export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}/kde \
	k3bsetup2dir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc k3b/{README,FAQ,ChangeLog,TODO}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/libk3baudiometainforenamerplugin.la
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%{_libdir}/kde3/kcm_k3bsetup2.la
%attr(755,root,root) %{_libdir}/kde3/kcm_k3bsetup2.so
%{_datadir}/applnk/.hidden/*.desktop
%dir %{_datadir}/apps/k3b
%{_datadir}/apps/k3b/cdi
%{_datadir}/apps/k3b/icons
%{_datadir}/apps/k3b/kpartplugins
%{_datadir}/apps/k3b/pics
%dir %{_datadir}/apps/k3b/plugins
%{_datadir}/apps/k3b/eventsrc
%{_datadir}/apps/k3b/k3bui.rc
%{_datadir}/apps/k3b/tips
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/mimelnk/application/x-k3b.desktop
%{_datadir}/sounds/*.wav
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/apps/k3b.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/libk3bcore.la
%attr(755,root,root) %{_libdir}/libk3bcore.so
%{_libdir}/libk3bdevice.la
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%{_libdir}/libk3bplugin.la
%attr(755,root,root) %{_libdir}/libk3bplugin.so
%{_libdir}/libk3bproject.la
%attr(755,root,root) %{_libdir}/libk3bproject.so
%{_libdir}/libk3btools.la
%attr(755,root,root) %{_libdir}/libk3btools.so

%files plugin-decoder-flac
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bflacdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bflacdecoder.so
%{_datadir}/apps/k3b/plugins/k3bflacdecoder.plugin

%files plugin-decoder-mad
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bmaddecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bmaddecoder.so
%{_datadir}/apps/k3b/plugins/k3bmaddecoder.plugin

%files plugin-decoder-oggvorbis
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3boggvorbisdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3boggvorbisdecoder.so
%{_datadir}/apps/k3b/plugins/k3boggvorbisdecoder.plugin

%files plugin-decoder-wave
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bwavedecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bwavedecoder.so
%{_datadir}/apps/k3b/plugins/k3bwavedecoder.plugin

%files plugin-encoder-lame
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3blameencoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3blameencoder.so
%{_datadir}/apps/k3b/plugins/k3blameencoder.plugin

%files plugin-encoder-external
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bexternalencoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bexternalencoder.so
%{_datadir}/apps/k3b/plugins/k3bexternalencoder.plugin

%files plugin-encoder-oggvorbis
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3boggvorbisencoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3boggvorbisencoder.so
%{_datadir}/apps/k3b/plugins/k3boggvorbisencoder.plugin

%files plugin-encoder-sox
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bsoxencoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bsoxencoder.so
%{_datadir}/apps/k3b/plugins/k3bsoxencoder.plugin
