#
# TODO & NOTES:
# - nas support is obsolete? it depends on kdelibs build type
# - it overrides rpm*flags (hardcoded -O2)
# - BR alsa-libs ? is this really needed?

%define		_snap		031107
%define		_ver		0.11
%define		_i18nver	0.10

Summary:	The CD Kreator
Summary(pl):	Kreator CD
Name:		k3b
Version:	0.11
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
# From kdeextragear-1 kde cvs module
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	442e8309ae7ad4b090a35c1d2fa294ee
Source1:	http://dl.sourceforge.net/sourceforge/k3b/%{name}-i18n-%{_i18nver}.tar.gz
# Source1-md5:	a14fd760bb146eaee22802c504e53152
URL:		http://k3b.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.1.92
BuildRequires:	libart_lgpl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
#BuildRequires:	nas-devel
Requires:	cdrdao >= 1.1.5
Requires:	cdrecord
Requires:	kdebase-core
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

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libk3bcore.

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
%setup -q -n %{name}-%{_snap} -a1

%build

# same thing as with kdemultimedia
# includes kernel headers which breaks things
# with PLD kernels 2.4.x, below workaround  by misiek
mkdir linux scsi
sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
/usr/include/linux/cdrom.h > linux/cdrom.h
cp /usr/include/scsi/scsi.h scsi

sed -i 's/AudioVideo/X-CD-RW/' src/%{name}.desktop

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--enable-final
	
%{__make}

cd %{name}-i18n-%{_i18nver}
%{__make} -f admin/Makefile.common
%configure
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir}

cd %{name}-i18n-%{_i18nver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/k3b.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/System/k3bsetup2.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde
	
sed -i 's/AudioVideo/X-CD-RW/' $RPM_BUILD_ROOT%{_desktopdir}/kde/k3b.desktop

echo "Categories=Qt;KDE;X-KDE-settings-system" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/k3bsetup2.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/k3b
%{_libdir}/libk3bcore.la
%attr(755,root,root) %{_libdir}/libk3bcore.so.*.*.*
%{_libdir}/libk3bplugin.la
%attr(755,root,root) %{_libdir}/libk3bplugin.so.*.*.*
%{_libdir}/libk3bproject.la
%attr(755,root,root) %{_libdir}/libk3bproject.so.*.*.*
%{_libdir}/libk3btools.la
%attr(755,root,root) %{_libdir}/libk3btools.so.*.*.*
%{_libdir}/libk3baudiometainforenamerplugin.la
%attr(755,root,root) %{_libdir}/libk3baudiometainforenamerplugin.so
%{_libdir}/kde3/kcm_k3bsetup2.la
%attr(755,root,root) %{_libdir}/kde3/kcm_k3bsetup2.so
%dir %{_datadir}/apps/k3b
%{_datadir}/apps/k3b/cdi
%{_datadir}/apps/k3b/icons
%{_datadir}/apps/k3b/kpartplugins
%{_datadir}/apps/k3b/pics
%{_datadir}/apps/k3b/eventsrc
%{_datadir}/apps/k3b/k3bui.rc
%{_datadir}/apps/k3b/tips
%dir %{_datadir}/apps/k3b/plugins
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/mimelnk/application/x-k3b.desktop
%{_datadir}/sounds/*.wav
%{_applnkdir}/.hidden/k3b-cue.desktop
%{_applnkdir}/.hidden/k3b-iso.desktop
%{_desktopdir}/kde/k3b.desktop
%{_desktopdir}/kde/k3bsetup2.desktop
%{_iconsdir}/hicolor/*/apps/k3b.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/libk3bcore.so
%{_libdir}/libk3bplugin.so
%{_libdir}/libk3bproject.so
%{_libdir}/libk3btools.so

%files plugin-decoder-mad
%defattr(644,root,root,755)
%{_libdir}/libk3bmaddecoder.la
%attr(755,root,root) %{_libdir}/libk3bmaddecoder.so
%{_datadir}/apps/k3b/plugins/k3bmaddecoder.plugin

%files plugin-decoder-oggvorbis
%defattr(644,root,root,755)
%{_libdir}/libk3boggvorbisdecoder.la
%attr(755,root,root) %{_libdir}/libk3boggvorbisdecoder.so
%{_datadir}/apps/k3b/plugins/k3boggvorbisdecoder.plugin

%files plugin-decoder-wave
%defattr(644,root,root,755)
%{_libdir}/libk3bwavedecoder.la
%attr(755,root,root) %{_libdir}/libk3bwavedecoder.so
%{_datadir}/apps/k3b/plugins/k3bwavedecoder.plugin

%files plugin-encoder-external
%defattr(644,root,root,755)
%{_libdir}/libk3bexternalencoder.la
%attr(755,root,root) %{_libdir}/libk3bexternalencoder.so
%{_datadir}/apps/k3b/plugins/k3bexternalencoder.plugin

%files plugin-encoder-oggvorbis
%defattr(644,root,root,755)
%{_libdir}/libk3boggvorbisencoder.la
%attr(755,root,root) %{_libdir}/libk3boggvorbisencoder.so
%{_datadir}/apps/k3b/plugins/k3boggvorbisencoder.plugin

%files plugin-encoder-sox
%defattr(644,root,root,755)
%{_libdir}/libk3bsoxencoder.la
%attr(755,root,root) %{_libdir}/libk3bsoxencoder.so
%{_datadir}/apps/k3b/plugins/k3bsoxencoder.plugin
