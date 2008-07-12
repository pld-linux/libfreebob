Summary:	FreeBoB - free driver implementation for the BeBoB platform
Summary(pl.UTF-8):	FreeBoB - wolnodostępna implementacja sterowników dla platformy BeBoB
Name:		libfreebob
Version:	1.0.11
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/freebob/%{name}-%{version}.tar.gz
# Source0-md5:	e49eed0084b9e793e7a0713aa99c196c
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

%description -l pl.UTF-8
Celem tego projektu jest zapewnienie wolnodostępnej implementacji
sterowników dla platformy BeBoB. BeBoB jest używana w wielu dostępnych
"break-out boksach" opartych na IEEE 1394.

%package devel
Summary:	Header files for FreeBoB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FreeBoB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libavc1394-devel >= 0.5.3
Requires:	libiec61883-devel >= 1.1.0
Requires:	libraw1394-devel >= 1.2.1
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.6.0

%description devel
Header files for FreeBoB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FreeBoB.

%package static
Summary:	Static FreeBoB library
Summary(pl.UTF-8):	Statyczna biblioteka FreeBoB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FreeBoB library.

%description static -l pl.UTF-8
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
%attr(755,root,root) %ghost %{_libdir}/libfreebob.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreebob.so
%{_libdir}/libfreebob.la
%{_includedir}/libfreebob
%{_pkgconfigdir}/libfreebob.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfreebob.a
