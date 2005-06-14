# TODO
#  - HAL support
#  - more decoder/encoder subpackages (mv from -devel)
#
# Conditional build:
%bcond_with	linux22		# building on kernel 2.2.x
%bcond_with	reqs		# force optional Requires
%bcond_without	resmgr		# build without ResMgr support
%bcond_without	setup		# don't build K3bSetup2 KControl Module
#
%define		_i18nver	0.12
Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.12
Release:	0.9
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{version}.tar.bz2
# Source0-md5:	df8f53698d28697213dfa6c9612bb249
Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-%{_i18nver}.tar.bz2
# Source1-md5:	9fb4531d43f5477368d2069e0ff4b876
Patch0:		%{name}-linux22.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-group.patch
Patch3:		%{name}-musepack.patch
URL:		http://www.k3b.org/
BuildRequires:	arts-qt-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.9.5
BuildRequires:	cdparanoia-III-devel
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	lame-libs-devel
BuildRequires:	libmusepack-devel >= 1.1
BuildRequires:	libmusicbrainz-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
%{?with_resmgr:BuildRequires:	resmgr-devel}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
Requires:	cdrdao >= 1.1.5
Requires:	cdrecord
Requires:	mkisofs
%if %{with reqs}
Requires:	normalize
Requires:	transcode >= 0.6.0
Requires:	vcdimager >= 0.7
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CD Kreator features:
 - the most userfriendly interface ever ;-)
 - writing audio-CDs
 - writing ISO-CDs
 - writing existing iso-images to CD
 - CD copy (data, audio, mixed mode)
 - blanking of CD-RWs
 - CD ripping to WAV
 - dvd ripping with the transcode tools
 - DivX/XviD encoding
 - K3b checks if the user inserted an empty disk
 - Retrieving CD info and toc
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
%{?with_resmgr:Requires:	resmgr-devel}

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libk3bcore.

%package plugin-decoder-flac
Summary:	Decoder plugin - FLAC
Summary(pl):	Wtyczka dekoduj±ca - FLAC
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-flac
Decoding module to decode FLAC files.

%description plugin-decoder-flac -l pl
Modu³ dekoduj±cy pliki w formacie FLAC.

%package plugin-decoder-mad
Summary:	Decoder plugin - mad
Summary(pl):	Wtyczka dekoduj±ca - mad
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-mad
Decoding module to decode MPEG 1 Layer III files.

%description plugin-decoder-mad -l pl
Modu³ dekoduj±cy pliki w formacie MPEG 1 Layer III.

%package plugin-decoder-musepack
Summary:	Decoder plugin - Musepack
Summary(pl):	Wtyczka dekoduj±ca - Musepack
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-musepack
Decoding module to decode Musepack files.

%description plugin-decoder-musepack -l pl
Modu³ dekoduj±cy pliki w formacie Musepack.

%package plugin-decoder-oggvorbis
Summary:	Decoder plugin - oggvorbis
Summary(pl):	Wtyczka dekoduj±ca - oggvorbis
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-oggvorbis
Decoding module to decode Ogg Vorbis files.

%description plugin-decoder-oggvorbis -l pl
Modu³ dekoduj±cy pliki w formacie Ogg Vorbis.

%package plugin-decoder-wave
Summary:	Decoder plugin - WAVE
Summary(pl):	Wtyczka dekoduj±ca - WAVE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-wave
Decoding module to decode WAVE files.

%description plugin-decoder-wave -l pl
Modu³ dekoduj±cy pliki w formacie WAVE.

%package plugin-encoder-external
Summary:	Encoder plugin - external
Summary(pl):	Wtyczka koduj±ca - external
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-encoder-external
Encoding module that allows specifying an encoding command.

%description plugin-encoder-external -l pl
Modu³ koduj±cy pozwalaj±cy na sformu³owanie komendy kodowania.

%package plugin-encoder-oggvorbis
Summary:	Encoder plugin - oggvorbis
Summary(pl):	Wtyczka koduj±ca - oggvorbis
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-encoder-oggvorbis
Encoding module to encode Ogg Vorbis files.

%description plugin-encoder-oggvorbis -l pl
Modu³ koduj±cy pliki w formacie Ogg Vorbis.

%package plugin-encoder-sox
Summary:	Encoder plugin - sox
Summary(pl):	Wtyczka koduj±ca - sox
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	sox

%description plugin-encoder-sox
Encoding module to encode many file formats using sox.

%description plugin-encoder-sox -l pl
Modu³ koduj±cy pliki w wielu formatach u¿ywaj±c programu sox.

%prep
%setup -q -a1
%{?with_linux22:%patch0 -p1}
#%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	%{!?with_resmgr:--without-resmgr} \
	%{!?with_setup:--with-k3bsetup=no}

%{__make}

cd %{name}-i18n-%{_i18nver}
cp -f /usr/share/automake/config.sub admin
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
	
%{__make} install -C %{name}-i18n-%{_i18nver} \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/k3b
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%{_libdir}/libk3baudiometainforenamerplugin.la
%{_datadir}/applnk/.hidden/*.desktop
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%dir %{_datadir}/apps/k3b
%dir %{_datadir}/apps/k3b/plugins
%{_datadir}/apps/k3b/*
%exclude %{_datadir}/apps/k3b/plugins/*
%{_datadir}/mimelnk/application/x-k3b.desktop
%{_datadir}/sounds/*.wav
%{_desktopdir}/kde/k3b.desktop
%{_iconsdir}/*/*/apps/k3b.png

%if %{with setup}
%attr(755,root,root) %{_bindir}/k3bsetup
%attr(755,root,root) %{_libdir}/kde3/kcm_*.so
%{_libdir}/kde3/kcm_*.la
%{_desktopdir}/kde/k3bsetup2.desktop
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libk3b.so
%{_libdir}/libk3b.la
%attr(755,root,root) %{_libdir}/libk3baudioprojectcddbplugin.so
%{_libdir}/libk3baudioprojectcddbplugin.la
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%{_libdir}/libk3bdevice.la
%attr(755,root,root) %{_libdir}/kde3/libk3bartsoutputplugin.so
%{_libdir}/kde3/libk3bartsoutputplugin.la
%attr(755,root,root) %{_libdir}/kde3/libk3bffmpegdecoder.so
%{_libdir}/kde3/libk3bffmpegdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3blameencoder.so
%{_libdir}/kde3/libk3blameencoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3blibsndfiledecoder.so
%{_libdir}/kde3/libk3blibsndfiledecoder.la
%{_includedir}/*.h

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

%files plugin-decoder-musepack
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bmpcdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bmpcdecoder.so
%{_datadir}/apps/k3b/plugins/k3bmpcdecoder.plugin

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
