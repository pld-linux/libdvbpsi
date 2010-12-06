#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for decoding and generation of MPEG TS and DVB PSI tables
Summary(pl.UTF-8):	Biblioteka do dekodowania i generowania tablic MPEG TS i DVB PSI
Name:		libdvbpsi
Version:	0.1.7
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.videolan.org/pub/libdvbpsi/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f2973c58635ff38df9e08440562b11bd
URL:		http://www.videolan.org/developers/libdvbpsi.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.

%description -l pl.UTF-8
libdvdpsi to bardzo prosta i przenośna biblioteka zaprojektowana do
dekodowania i generowania tablic MPEG TS i DVB PSI.

%package devel
Summary:	Header files for libdvbpsi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdvbpsi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdvbpsi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdvbpsi.

%package static
Summary:	Static libdvbpsi library
Summary(pl.UTF-8):	Statyczna biblioteka libdvbpsi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdvbpsi library.

%description static -l pl.UTF-8
Statyczna biblioteka libdvbpsi.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libdvbpsi.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvbpsi.so
%{_libdir}/libdvbpsi.la
%{_includedir}/dvbpsi
%{_pkgconfigdir}/libdvbpsi.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdvbpsi.a
%endif
