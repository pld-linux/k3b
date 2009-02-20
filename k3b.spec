
%define		_qtver	4.4.3
%define		_snap 925654

Summary:	The CD Kreator
Summary(pl.UTF-8):	Kreator CD
Name:		k3b
Version:	1.95
Release:	0.%{_snap}.3
License:	GPL v2+
Group:		X11/Libraries
Source0:	k3b-%{version}-%{_snap}.tar.bz2
# Source0-md5:	371d0a6f8a332e9820a561d3c6df4caf
URL:		http://k3b.plainblack.com/
BuildRequires:	QtNetwork-devel >= %{_qtver}
BuildRequires:	QtOpenGL-devel >= %{_qtver}
BuildRequires:	QtScript-devel >= %{_qtver}
BuildRequires:	QtSql-devel >= %{_qtver}
BuildRequires:	QtSvg-devel >= %{_qtver}
BuildRequires:	QtTest-devel >= %{_qtver}
BuildRequires:	QtUiTools-devel >= %{_qtver}
BuildRequires:	QtWebKit-devel >= %{_qtver}
BuildRequires:	kde4-kdemultimedia-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	taglib-devel
Suggests:	cdrdao
Suggests:	cdrtools
Suggests:	dvd+rw-tools
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
%setup -q -n %{name}-%{version}-%{_snap}
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
%attr(755,root,root) %{_libdir}/kde4/k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bmaddecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bsoxencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bwavedecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bffmpegdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bmpcdecoder.desktop
%attr(755,root,root) %{_libdir}/kde4/k3bmpcdecoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bsetup2.so
%attr(755,root,root) %{_libdir}/kde4/kio_videodvd.so
%attr(755,root,root) %ghost %{_libdir}/libk3b.so.4
%attr(755,root,root) %{_libdir}/libk3b.so.4.0.0
%attr(755,root,root) %ghost %{_libdir}/libk3bdevice.so.6
%attr(755,root,root) %{_libdir}/libk3bdevice.so.6.0.0
%attr(755,root,root) %{_libdir}/kde4/k3blibsndfiledecoder.so
%{_desktopdir}/kde4/k3b.desktop
%{_datadir}/apps/k3b
%{_iconsdir}/hicolor/*x*/apps/k3b.png
%{_datadir}/kde4/services/ServiceMenus/k3b_audiocd_rip.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_cd_copy.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_dvd_copy.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_handle_empty_cd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_handle_empty_dvd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_videodvd_rip.desktop
%{_datadir}/kde4/services/k3bexternalencoder.desktop
%{_datadir}/kde4/services/k3blameencoder.desktop
%{_datadir}/kde4/services/k3blibsndfiledecoder.desktop
%{_datadir}/kde4/services/k3bmaddecoder.desktop
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
%{_datadir}/sounds/k3b*.wav
