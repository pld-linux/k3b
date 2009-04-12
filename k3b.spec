
%define		qtver	4.5.0
%define		snap 948635

%define		rel	3
Summary:	The CD Kreator
Summary(pl.UTF-8):	Kreator CD
Name:		k3b
Version:	2.0
Release:	0.%{snap}.%{rel}
License:	GPL v2+
Group:		X11/Libraries
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	160f13bfa0bfc7c95dc05616163cc34f
URL:		http://k3b.plainblack.com/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	flac-c++-devel
BuildRequires:	kde4-kdemultimedia-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	taglib-devel
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

%prep
%setup -q -n %{name}-%{version}-%{snap}
%{__sed} -i -e 's@Exec=k3bsetup@Exec=k3bsetup2@g' k3bsetup/k3bsetup2.desktop

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
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
%attr(755,root,root) %{_libdir}/kde4/k3bffmpegdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bmpcdecoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bsetup2.so
%attr(755,root,root) %{_libdir}/kde4/kio_videodvd.so
%attr(755,root,root) %ghost %{_libdir}/libk3b.so.6
%attr(755,root,root) %{_libdir}/libk3b.so.6.0.0
%attr(755,root,root) %ghost %{_libdir}/libk3bdevice.so.6
%attr(755,root,root) %{_libdir}/libk3bdevice.so.6.0.0
%attr(755,root,root) %{_libdir}/kde4/k3blibsndfiledecoder.so
%{_desktopdir}/kde4/k3b.desktop
%{_datadir}/apps/k3b
%{_iconsdir}/hicolor/*x*/apps/k3b.png

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
%{_datadir}/kde4/services/k3bsetup2.desktop
%{_datadir}/kde4/services/k3bsoxencoder.desktop
%{_datadir}/kde4/services/k3bwavedecoder.desktop
%{_datadir}/kde4/services/k3bffmpegdecoder.desktop
%{_datadir}/kde4/services/kcm_k3bexternalencoder.desktop
%{_datadir}/kde4/services/kcm_k3blameencoder.desktop
%{_datadir}/kde4/services/kcm_k3boggvorbisencoder.desktop
%{_datadir}/kde4/services/videodvd.protocol
%{_datadir}/kde4/servicetypes/k3bplugin.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/sounds/k3b*.wav
