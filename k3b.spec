#
# TODO: fill R: of -devel subpackage
# - k3b-1.91.0-0.rc2.1.i686: required "/usr/share/apps/konqsidebartng/virtual_folders/services" is provided by following packages:
#   a) kde4-kdebase-workspace-4.4.2-3.i686
#   b) kde4-kdebase-workspace-4.4.1-1.i686
#   c) kde4-konqueror-4.4.2-1.i686
#   d) kde4-konqueror-4.4.1-1.i686

%bcond_without	ffmpeg

%define		qtver	4.6.3
%define		kdever	4.4.5

Summary:	The CD Kreator
Summary(hu.UTF-8):	CD Kreator
Summary(pl.UTF-8):	Kreator CD
Name:		k3b
Version:	2.0.3
Release:	4
Epoch:		1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/k3b/%{name}-%{version}a.tar.xz
# Source0-md5:	52e78aabe8e483347d04e88be0aed150
Patch0:		cmake-duplicate-doc.patch
Patch1:		ffmpeg3.patch
Patch2:		musepack.patch
URL:		http://k3b.plainblack.com/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	flac-c++-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-libkcddb-devel >= %{kdever}
BuildRequires:	libdvdread-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmusicbrainz-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	musepack-devel
BuildRequires:	polkit-qt-devel >= 0.9.2
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	taglib-devel
Requires:	kde4-kdebase-runtime
Suggests:	cdrdao
Suggests:	cdrtools
Suggests:	dvd+rw-tools
Obsoletes:	k3b-plugin-decoder-ffmpeg
Obsoletes:	k3b-plugin-decoder-flac
Obsoletes:	k3b-plugin-decoder-libsndfile
Obsoletes:	k3b-plugin-decoder-mad
Obsoletes:	k3b-plugin-decoder-musepack
Obsoletes:	k3b-plugin-decoder-oggvorbis
Obsoletes:	k3b-plugin-decoder-wave
Obsoletes:	k3b-plugin-encoder-external
Obsoletes:	k3b-plugin-encoder-lame
Obsoletes:	k3b-plugin-encoder-oggvorbis
Obsoletes:	k3b-plugin-encoder-sox
Obsoletes:	k3b-plugin-konqueror
Obsoletes:	k3b-plugin-output-alsa
Obsoletes:	k3b-plugin-output-arts
Obsoletes:	k3b-plugin-project
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

%description -l hu.UTF-8
A CD Kreator lehetőségei:
 - a legfelhasználóbarátabb felület ;-)
 - audio CD-k írása
 - ISO CD-k írása
 - iso-képek írása CD-re
 - CD másolás (adat, audio, vegyes)
 - CD-RW-k törlése
 - CD rippelése WAV-ba
 - dvd rippelése
 - DivX/XviD kódolás
 - k3b ellenőrzi, hogy van-e a gépben üres lemez
 - CD infomráció és toc lekérdezése
 - ATAPI támogatás SCSI-emuláció nélkül az olvasáshoz
 - audiolejátszó

%description -l pl.UTF-8
Własności Kreatora CD:
 - najbardziej przyjazny dla użytkownika interfejs ;-)
 - zapisywanie płyt CD-Audio
 - zapisywanie płyt ISO
 - zapisywanie istniejących obrazów ISO na CD
 - kopiowanie CD (data/audio/mixed - z danymi, dźwiękiem i mieszane)
 - czyszczenie płyt CD-RW
 - rippowanie CD do plików WAV
 - rippowanie DVD przy użyciu narzędzi transcode
 - kodowanie DivX/XviD
 - sprawdzanie, czy użytkownik włożył czystą płytę
 - odtwarzania CD-info i TOC
 - obsługa nagrywarek ATAPI bez emulacji SCSI przy odczycie
 - zintegrowany odtwarzacz płyt audio o pełnych możliwościach

%package devel
Summary:	Header files for libk3bcore library
Summary(hu.UTF-8):	Fejléc fájlok (libk3bcore)
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libk3bcore
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libdvdread-devel
Requires:	libsamplerate-devel

%description devel
Header files for libk3bcore library.

%description devel -l hu.UTF-8
Fejléc fájlok a libk3bcore-hoz.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libk3bcore.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake \
	%{!?with_ffmpeg:-DK3B_BUILD_FFMPEG_DECODER_PLUGIN=no} \
	-DK3B_ENABLE_HAL_SUPPORT=no \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# remove unsupported langs
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/sr@ijekavian
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/sr@ijekavianlatin

%find_lang %{name} --all-name --with-kde

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/k3b
%attr(755,root,root) %{_bindir}/k3bsetup
%attr(755,root,root) %{_libdir}/kde4/k3baudiometainforenamerplugin.so
%attr(755,root,root) %{_libdir}/kde4/k3baudioprojectcddbplugin.so
%attr(755,root,root) %{_libdir}/kde4/k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bflacdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bmaddecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bsoxencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bwavedecoder.so
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/kde4/k3bffmpegdecoder.so}
%attr(755,root,root) %{_libdir}/kde4/k3bmpcdecoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bsetup.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bsoxencoder.so
%attr(755,root,root) %{_libdir}/kde4/kio_videodvd.so
%attr(755,root,root) %ghost %{_libdir}/libk3blib.so.6
%attr(755,root,root) %{_libdir}/libk3blib.so.6.0.0
%attr(755,root,root) %ghost %{_libdir}/libk3bdevice.so.6
%attr(755,root,root) %{_libdir}/libk3bdevice.so.6.0.0
%attr(755,root,root) %{_libdir}/kde4/k3blibsndfiledecoder.so
%attr(755,root,root) %{_libdir}/kde4/libexec/k3bsetuphelper
%{_desktopdir}/kde4/k3b.desktop
%{_datadir}/apps/k3b
%{_iconsdir}/hicolor/*x*/apps/k3b.png
%{_iconsdir}/hicolor/scalable/apps/k3b.svgz

%{_datadir}/apps/solid/actions/k3b_audiocd_rip.desktop
%{_datadir}/apps/solid/actions/k3b_copy_disc.desktop
%{_datadir}/apps/solid/actions/k3b_create_audio_cd_from_blank_medium.desktop
%{_datadir}/apps/solid/actions/k3b_create_data_project_from_blank_medium.desktop
%{_datadir}/apps/solid/actions/k3b_videodvd_rip.desktop

%{_datadir}/kde4/services/ServiceMenus/k3b_create_audio_cd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_create_data_project.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_create_video_cd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_write_bin_image.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_write_iso_image.desktop
%{_datadir}/kde4/services/k3baudiometainforenamerplugin.desktop
%{_datadir}/kde4/services/k3baudioprojectcddbplugin.desktop
%{_datadir}/kde4/services/k3bexternalencoder.desktop
%{_datadir}/kde4/services/k3bflacdecoder.desktop
%{_datadir}/kde4/services/k3blameencoder.desktop
%{_datadir}/kde4/services/k3blibsndfiledecoder.desktop
%{_datadir}/kde4/services/k3bmaddecoder.desktop
%{_datadir}/kde4/services/k3bmpcdecoder.desktop
%{_datadir}/kde4/services/k3boggvorbisdecoder.desktop
%{_datadir}/kde4/services/k3boggvorbisencoder.desktop
%{_datadir}/kde4/services/k3bsetup.desktop
%{_datadir}/kde4/services/k3bsoxencoder.desktop
%{_datadir}/kde4/services/k3bwavedecoder.desktop
%{?with_ffmpeg:%{_datadir}/kde4/services/k3bffmpegdecoder.desktop}
%{_datadir}/kde4/services/kcm_k3bexternalencoder.desktop
%{_datadir}/kde4/services/kcm_k3blameencoder.desktop
%{_datadir}/kde4/services/kcm_k3boggvorbisencoder.desktop
%{_datadir}/kde4/services/kcm_k3bsoxencoder.desktop
%{_datadir}/kde4/services/videodvd.protocol
%{_datadir}/kde4/servicetypes/k3bplugin.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
#%%{_datadir}/sounds/k3b*.wav
%{_datadir}/mime/packages/x-k3b.xml
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.k3bsetup.service
/etc/dbus-1/system.d/org.kde.kcontrol.k3bsetup.conf
%{_datadir}/polkit-1/actions/org.kde.kcontrol.k3bsetup.policy

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libk3blib.so
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%{_includedir}/*.h
