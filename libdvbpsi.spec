Summary:	Library for decoding and generation of MPEG TS and DVB PSI tables
Summary(pl):	Biblioteka do dekodowania i generowania tablic MPEG TS i DVB PSI
Name:		libdvbpsi
Version:	0.1.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.videolan.org/pub/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1d709d1e18228c413ad246165d8819c1
URL:		http://developers.videolan.org/libdvbpsi/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.

%description -l pl
libdvdpsi to bardzo prosta i przeno¶na biblioteka zaprojektowana do
dekodowania i generowania tablic MPEG TS i DVB PSI.

%package devel
Summary:	Header files for libdvbpsi library
Summary(pl):	Pliki nag³ówkowe biblioteki libdvbpsi
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libdvbpsi library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libdvbpsi.

%package static
Summary:	Static libdvbpsi library
Summary(pl):	Statyczna biblioteka libdvbpsi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libdvbpsi library.

%description static -l pl
Statyczna biblioteka libdvbpsi.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libdvbpsi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvbpsi.so
%{_libdir}/libdvbpsi.la
%{_includedir}/dvbpsi

%files static
%defattr(644,root,root,755)
%{_libdir}/libdvbpsi.a
