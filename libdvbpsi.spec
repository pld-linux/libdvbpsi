Summary:	-
Summary(pl):	-
Name:		libdvbpsi
Version:	0.1.3
Release:	1
License:	GPL
Group:		Multimedia
######		Unknown group!
Source0:	http://www.videolan.org/pub/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1d709d1e18228c413ad246165d8819c1
URL:		http://developers.videolan.org/libdvbpsi/
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.

%description -l pl


%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_includedir}/dvbpsi
%{_libdir}/%{name}.so*
