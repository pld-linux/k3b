#
# Conditional build:
%bcond_with	reqs		# force optional Requires
%bcond_without	setup		# don't build K3bSetup2 KControl Module
%bcond_with	linux22		# building on kernel 2.2.x
#
%define		_i18nver	0.11
Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.11.13
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/k3b/%{name}-%{version}.tar.bz2
# Source0-md5:	334a0545e42b77846f1eab1b67ef6c28
Source1:	http://dl.sourceforge.net/k3b/%{name}-i18n-%{_i18nver}.tar.bz2
# Source1-md5:	80d1ac1766ad8a8cdadca5f4273f2d95
Patch0:		%{name}-linux22.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-am19.patch
URL:		http://k3b.sourceforge.net/
BuildRequires:	arts-qt-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	cdparanoia-III-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
BuildRequires:	qt-devel >= 3.1
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
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libk3bcore.

%package plugin-decoder-flac
Summary:	Decoder plugin - flac
Summary(pl):	Wtyczka dekoduj±ca - flac
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-flac
Decoding module to decode FLAC files.
 
%description plugin-decoder-flac -l pl
Modu³ dekodujacy pliki w formacie FLAC.

%package plugin-decoder-mad
Summary:	Decoder plugin - mad
Summary(pl):	Wtyczka dekoduj±ca - mad
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-mad
Decoding module to decode MPEG 1 Layer III files.
 
%description plugin-decoder-mad -l pl
Modu³ dekodujacy pliki w formacie MPEG 1 Layer III.

%package plugin-decoder-oggvorbis
Summary:	Decoder plugin - oggvorbis
Summary(pl):	Wtyczka dekoduj±ca - oggvorbis
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-oggvorbis
Decoding module to decode Ogg Vorbis files.
 
%description plugin-decoder-oggvorbis -l pl
Modu³ dekodujacy pliki w formacie Ogg Vorbis.

%package plugin-decoder-wave
Summary:	Decoder plugin - wave
Summary(pl):	Wtyczka dekoduj±ca - wave
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-decoder-wave
Decoding module to decode wave files.
 
%description plugin-decoder-wave -l pl
Modu³ dekodujacy pliki w formacie wave.

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
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README FAQ ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
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
