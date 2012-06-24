Summary:	FreeBoB - free driver implementation for the BeBoB platform
Summary(pl):	FreeBoB - wolnodost�pna implementacja sterownik�w dla platformy BeBoB
Name:		libfreebob
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/freebob/%{name}-%{version}.tar.bz2
# Source0-md5:	c5ccd2f4353454acba50e53734742551
URL:		http://freebob.sourceforge.net/
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	libavc1394-devel >= 0.5.3
BuildRequires:	libiec61883-devel >= 1.1.0
BuildRequires:	libraw1394-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide a free driver implemenation for the BeBoB
platform. The BeBoB is used in many available IEEE 1394 based
break-out boxes.

%description -l pl
Celem tego projektu jest zapewnienie wolnodost�pnej implementacji
sterownik�w dla platformy BeBoB. BeBoB jest u�ywana w wielu dost�pnych
"break-out boksach" opartych na IEEE 1394.

%package devel
Summary:	Header files for FreeBoB library
Summary(pl):	Pliki nag��wkowe biblioteki FreeBoB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libavc1394-devel >= 0.5.3
Requires:	libiec61883-devel >= 1.1.0
Requires:	libraw1394-devel >= 1.2.1
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.6.0

%description devel
Header files for FreeBoB library.

%description devel -l pl
Pliki nag��wkowe biblioteki FreeBoB.

%package static
Summary:	Static FreeBoB library
Summary(pl):	Statyczna biblioteka FreeBoB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FreeBoB library.

%description static -l pl
Statyczna biblioteka FreeBoB.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libfreebob.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreebob.so
%{_libdir}/libfreebob.la
%{_includedir}/libfreebob
%{_pkgconfigdir}/libfreebob.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfreebob.a
