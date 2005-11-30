#
# Conditional build:
%bcond_with	linux22		# building on kernel 2.2.x
%bcond_with	reqs		# force optional Requires
%bcond_without	resmgr		# build without ResMgr support
%bcond_without	setup		# don't build K3bSetup2 KControl Module
#
%define		_kdever		9:3.2
Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.12.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{version}.tar.bz2
# Source0-md5:	dff0c2075266e6ad5d3c4ad99bcf8a54
Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-%{version}.tar.bz2
# Source1-md5:	eea7b0026cc1c34c4ca4bdd09d0eda0d
Patch0:		%{name}-linux22.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-group.patch
URL:		http://www.k3b.org/
BuildRequires:	acl-devel
BuildRequires:	arts-qt-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9.4
BuildRequires:	dbus-qt-devel >= 0.33
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	gettext-devel
BuildRequires:	hal-devel >= 0.4
BuildRequires:	kdelibs-devel >= %{_kdever}
BuildRequires:	lame-libs-devel
BuildRequires:	libmpcdec-devel
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

%package plugin-decoder-ffmpeg
Summary:	Decoder plugin - FFMpeg
Summary(pl):	Wtyczka dekoduj±ca - FFMpeg
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-ffmpeg
Decoding module to decode WMA (and others) files.

%description plugin-decoder-ffmpeg -l pl
Modu³ dekoduj±cy pliki w formacie WMA (i nie tylko).

%package plugin-decoder-flac
Summary:	Decoder plugin - FLAC
Summary(pl):	Wtyczka dekoduj±ca - FLAC
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-flac
Decoding module to decode FLAC files.

%description plugin-decoder-flac -l pl
Modu³ dekoduj±cy pliki w formacie FLAC.

%package plugin-decoder-libsndfile
Summary:	Decoder plugin - libsndfile
Summary(pl):	Wtyczka dekoduj±ca - libsndfile
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-libsndfile
Decoding module to decode audio files supported by libsndfile.

%description plugin-decoder-libsndfile -l pl
Modu³ dekoduj±cy pliki audio obs³ugiwane przez bibliotekê libsndfile.

%package plugin-decoder-mad
Summary:	Decoder plugin - mad
Summary(pl):	Wtyczka dekoduj±ca - mad
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-mad
Decoding module to decode MPEG-1 Layer III files.

%description plugin-decoder-mad -l pl
Modu³ dekoduj±cy pliki w formacie MPEG-1 Layer III.

%package plugin-decoder-musepack
Summary:	Decoder plugin - Musepack
Summary(pl):	Wtyczka dekoduj±ca - Musepack
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-musepack
Decoding module to decode Musepack audio files.

%description plugin-decoder-musepack -l pl
Modu³ dekoduj±cy pliki audio w formacie Musepack.

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

%package plugin-encoder-lame
Summary:	Encoder plugin - lame
Summary(pl):	Wtyczka koduj±ca - lame
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-encoder-lame
Encoding module to encode MPEG-1 Layer III (mp3) files.

%description plugin-encoder-lame -l pl
Modu³ koduj±cy pliki w formacie MPEG-1 Layer III (mp3).

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
Modu³ koduj±cy pliki w wielu formatach przy u¿yciu programu sox.

%package plugin-konqueror
Summary:	Plugins extending the functionality of Konqueror
Summary(pl):	Wtyczki rozszerzaj±ce funkcjonalno¶æ Konquerora
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	konqueror >= %{_kdever}

%description plugin-konqueror
Package contains plugins (but accurately "servicemenus") extending the
functionality of Konqueror.

%description plugin-konqueror -l pl
Pakiet zawiera wtyczki (a dok³adniej "servicemenus") rozszerzaj±ce
funkcjonalno¶æ Konquerora.

%package plugin-output-arts
Summary:	Plugin - arts support
Summary(pl):	Wtyczka - obs³uga arts
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-output-arts
Audio Output plugin which plays through arts.

%description plugin-output-arts -l pl
Wtyczka odtwarzania d¼wiêku przez arts.

%package plugin-project
Summary:	Additional plugins from group project
Summary(pl):	Dodatkowe wtyczki z grupy projekt
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-project
Additional plugins from group project:
Audio Metainfo Renamer, Cddb Audio Plugin.

%description plugin-project -l pl
Dodatkowe wtyczki z grupy projekt:
Audio Metainfo Renamer, Cddb Audio Plugin.

%prep
%setup -q -a1
%{?with_linux22:%patch0 -p1}
%patch1 -p1
%patch2 -p1

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

cd %{name}-i18n-%{version}
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

%{__make} install -C %{name}-i18n-%{version} \
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
%{_datadir}/applnk/.hidden/*.desktop
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
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%{_libdir}/libk3b.la
%{_libdir}/libk3bdevice.la
%{_includedir}/*.h

%files plugin-decoder-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bffmpegdecoder.so
%{_libdir}/kde3/libk3bffmpegdecoder.la
%{_datadir}/apps/k3b/plugins/k3bffmpegdecoder.plugin

%files plugin-decoder-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bflacdecoder.so
%{_libdir}/kde3/libk3bflacdecoder.la
%{_datadir}/apps/k3b/plugins/k3bflacdecoder.plugin

%files plugin-decoder-libsndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3blibsndfiledecoder.so
%{_libdir}/kde3/libk3blibsndfiledecoder.la
%{_datadir}/apps/k3b/plugins/k3blibsndfiledecoder.plugin

%files plugin-decoder-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bmaddecoder.so
%{_libdir}/kde3/libk3bmaddecoder.la
%{_datadir}/apps/k3b/plugins/k3bmaddecoder.plugin

%files plugin-decoder-musepack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bmpcdecoder.so
%{_libdir}/kde3/libk3bmpcdecoder.la
%{_datadir}/apps/k3b/plugins/k3bmpcdecoder.plugin

%files plugin-decoder-oggvorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3boggvorbisdecoder.so
%{_libdir}/kde3/libk3boggvorbisdecoder.la
%{_datadir}/apps/k3b/plugins/k3boggvorbisdecoder.plugin

%files plugin-decoder-wave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bwavedecoder.so
%{_libdir}/kde3/libk3bwavedecoder.la
%{_datadir}/apps/k3b/plugins/k3bwavedecoder.plugin

%files plugin-encoder-external
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bexternalencoder.so
%{_libdir}/kde3/libk3bexternalencoder.la
%{_datadir}/apps/k3b/plugins/k3bexternalencoder.plugin

%files plugin-encoder-lame
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3blameencoder.so
%{_libdir}/kde3/libk3blameencoder.la
%{_datadir}/apps/k3b/plugins/k3blameencoder.plugin

%files plugin-encoder-oggvorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3boggvorbisencoder.so
%{_libdir}/kde3/libk3boggvorbisencoder.la
%{_datadir}/apps/k3b/plugins/k3boggvorbisencoder.plugin

%files plugin-encoder-sox
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bsoxencoder.so
%{_libdir}/kde3/libk3bsoxencoder.la
%{_datadir}/apps/k3b/plugins/k3bsoxencoder.plugin

%files plugin-konqueror
%defattr(644,root,root,755)
%{_datadir}/apps/konqueror/servicemenus/*.desktop

%files plugin-output-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libk3bartsoutputplugin.so
%{_libdir}/kde3/libk3bartsoutputplugin.la
%{_datadir}/apps/k3b/plugins/k3bartsoutputplugin.plugin

%files plugin-project
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%attr(755,root,root) %{_libdir}/libk3baudioprojectcddbplugin.so
%{_libdir}/libk3baudiometainforenamerplugin.la
%{_libdir}/libk3baudioprojectcddbplugin.la
%{_datadir}/apps/k3b/plugins/k3baudiometainforenamerplugin.plugin
%{_datadir}/apps/k3b/plugins/k3baudioprojectcddbplugin.plugin
