#
# Conditional build:
%bcond_with	reqs		# force optional Requires
%bcond_without	resmgr		# build without ResMgr support
%bcond_without	setup		# don't build K3bSetup2 KControl Module
#
%define		_i18nver	0.11
%define		_snap	050525
Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.11.99
Release:	0.%{_snap}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{_snap}.tar.bz2
# Source0-md5:	2b4fb811f2d5419804fe8914868c7a2d
# Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-%{_i18nver}.tar.bz2
# Source1-md5:	80d1ac1766ad8a8cdadca5f4273f2d95
Patch0:		%{name}-group.patch
Patch1:		kde-common-gcc4.patch
URL:		http://www.k3b.org/
BuildRequires:	arts-qt-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	cdparanoia-III-devel
BuildRequires:	flac-devel
BuildRequires:	lame-libs-devel
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	kdelibs-devel >= 9:3.1
BuildRequires:	libsamplerate-devel
%{?with_resmgr:BuildRequires:	resmgr-devel}
BuildRequires:	rpmbuild(macros) >= 1.129
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

%package plugin-decoder-ffmpeg
Summary:	Decoder plugin - ffmpeg
Summary(pl):	Wtyczka dekoduj±ca - ffmpeg
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-ffmpeg
Decoding module to decode MPEG 1 Layer III files.
 
%description plugin-decoder-ffmpeg -l pl
Modu³ dekoduj±cy pliki w formacie MPEG 1 Layer III.

%package plugin-decoder-mad
Summary:	Decoder plugin - mad
Summary(pl):	Wtyczka dekoduj±ca - mad
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-mad
Decoding module to decode MPEG 1 Layer III files.
 
%description plugin-decoder-mad -l pl
Modu³ dekoduj±cy pliki w formacie MPEG 1 Layer III.

%package plugin-decoder-mpc
Summary:	Decoder plugin - mpc
Summary(pl):	Wtyczka dekoduj±ca - mpc
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-mpc
Decoding module to decode MPEG 1 Layer III files.
 
%description plugin-decoder-mpc -l pl
Modu³ dekoduj±cy pliki w formacie MPEG 1 Layer III.

%package plugin-decoder-oggvorbis
Summary:	Decoder plugin - oggvorbis
Summary(pl):	Wtyczka dekoduj±ca - oggvorbis
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-oggvorbis
Decoding module to decode Ogg Vorbis files.
 
%description plugin-decoder-oggvorbis -l pl
Modu³ dekoduj±cy pliki w formacie Ogg Vorbis.

%package plugin-decoder-sndfile
Summary:	Decoder plugin - sndfile
Summary(pl):	Wtyczka dekoduj±ca - sndfile
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-sndfile
Decoding module to decode MPEG 1 Layer III files.
 
%description plugin-decoder-sndfile -l pl
Modu³ dekoduj±cy pliki w formacie MPEG 1 Layer III.

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
Requires:	lame-libs

%description plugin-encoder-lame
Encoding module to encode many file formats using lame.
 
%description plugin-encoder-lame -l pl
Modu³ koduj±cy pliki w wielu formatach u¿ywaj±c programu lame.

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

%package plugin-output-arts
Summary:	Output plugin - arts
Summary(pl):	Wtyczka odtwarzaj±ca - arts
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	arts

%description plugin-output-arts
Output module to play using arts.
 
%description plugin-output-arts -l pl
Modu³ odtwarzaj±cy pliki u¿ywaj±c programu arts.

%prep
#setup -q -a1
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%{__sed} -i -e "s,K3bSetup 2 - ,,g" \
	-e 's/Categories=.*/Categories=Qt;KDE;X-KDE-settings-system;/g' \
	k3b/k3bsetup/k3bsetup2.desktop
	

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;DiscBurning;/g' \
	k3b/src/k3b.desktop

# use mpcdec as it should	
%{__sed} -i -e 's,musepack,mpcdec,g' k3b/configure.in.in \
	k3b/plugins/decoder/musepack/Makefile.am \
	k3b/plugins/decoder/musepack/k3bmpcwrapper.h

# fix gcc4 blabber
%{__sed} -i -e 's,BOOL,mpc_bool_t,g' \
	k3b/plugins/decoder/musepack/k3bmpcwrapper.cpp


%build
#cp -f /usr/share/automake/config.sub admin
#%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64  \
%endif
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	%{!?with_resmgr:--without-resmgr} \
	%{!?with_setup:--with-k3bsetup=no}

%{__make}

# cd %{name}-i18n-%{_i18nver}
# cp -f /usr/share/automake/config.sub admin
# %{__make} -f admin/Makefile.common
# %configure
# %{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}/kde \
	k3bsetup2dir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}
	
#%{__make} install -C %{name}-i18n-%{_i18nver} \
#	DESTDIR=$RPM_BUILD_ROOT \
#	kde_htmldir=%{_kdedocdir}

#rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx
#mv -f $RPM_BUILD_ROOT%{_datadir}/locale/ve{n,}

#find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc README FAQ ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%attr(755,root,root) %{_libdir}/libk3baudioprojectcddbplugin.so
%{_libdir}/libk3baudioprojectcddbplugin.la
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
#%attr(755,root,root) %{_libdir}/libk3bcore.so
#%{_libdir}/libk3bcore.la
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%{_libdir}/libk3bdevice.la
#%attr(755,root,root) %{_libdir}/libk3bplugin.so
#%{_libdir}/libk3bplugin.la
#%attr(755,root,root) %{_libdir}/libk3bproject.so
#%{_libdir}/libk3bproject.la
#%attr(755,root,root) %{_libdir}/libk3btools.so
#%{_libdir}/libk3btools.la
%{_includedir}/*.h

%files plugin-decoder-flac
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bflacdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bflacdecoder.so
%{_datadir}/apps/k3b/plugins/k3bflacdecoder.plugin

%files plugin-decoder-ffmpeg
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bffmpegdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bffmpegdecoder.so
%{_datadir}/apps/k3b/plugins/k3bffmpegdecoder.plugin

%files plugin-decoder-mad
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bmaddecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bmaddecoder.so
%{_datadir}/apps/k3b/plugins/k3bmaddecoder.plugin

%files plugin-decoder-mpc
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bmpcdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3bmpcdecoder.so
%{_datadir}/apps/k3b/plugins/k3bmpcdecoder.plugin

%files plugin-decoder-oggvorbis
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3boggvorbisdecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3boggvorbisdecoder.so
%{_datadir}/apps/k3b/plugins/k3boggvorbisdecoder.plugin

%files plugin-decoder-sndfile
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3blibsndfiledecoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3blibsndfiledecoder.so
%{_datadir}/apps/k3b/plugins/k3blibsndfiledecoder.plugin

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

%files plugin-encoder-lame
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3blameencoder.la
%attr(755,root,root) %{_libdir}/kde3/libk3blameencoder.so
%{_datadir}/apps/k3b/plugins/k3blameencoder.plugin

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

%files plugin-output-arts
%defattr(644,root,root,755)
%{_libdir}/kde3/libk3bartsoutputplugin.la
%attr(755,root,root) %{_libdir}/kde3/libk3bartsoutputplugin.so
%{_datadir}/apps/k3b/plugins/k3bartsoutputplugin.plugin
