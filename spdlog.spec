#
# Conditional build:
%bcond_with	cxx20	# C++ 20 std::format instead of libfmt (users of library must be built with C++20 too)

Summary:	Very fast C++ logging library
Summary(pl.UTF-8):	Bardzo szybka biblioteka C++ do logowania
Name:		spdlog
Version:	1.17.0
Release:	1
Epoch:		1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/gabime/spdlog/releases
Source0:	https://github.com/gabime/spdlog/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f0d8dd02539fe609bdfd42c0549fe28d
URL:		https://github.com/gabime/spdlog
BuildRequires:	cmake >= 3.10
%if %{with cxx20}
BuildRequires:	libstdc++-devel >= 6:13
%else
BuildRequires:	libfmt-devel >= 12.1
BuildRequires:	libstdc++-devel >= 6:4.7
%endif
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{without cxx20}
Requires:	libfmt >= 12.1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very fast C++ logging library.

%description -l pl.UTF-8
Bardzo szybka, składająca się z samych nagłówków biblioteka C++ do
logowania.

%package devel
Summary:	Very fast C++ logging library
Summary(pl.UTF-8):	Bardzo szybka biblioteka C++ do logowania
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%if %{with cxx20}
Requires:	libstdc++-devel >= 6:13
%else
Requires:	libfmt-devel >= 12.1
Requires:	libstdc++-devel >= 6:4.7
%endif

%description devel
Very fast C++ logging library.

%description devel -l pl.UTF-8
Bardzo szybka, składająca się z samych nagłówków biblioteka C++ do
logowania.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
%if %{with cxx20}
	-DSPDLOG_USE_STD_FORMAT=ON \
%else
	-DSPDLOG_FMT_EXTERNAL=ON
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_libdir}/libspdlog.so.*.*.*
%ghost %{_libdir}/libspdlog.so.1.17

%files devel
%defattr(644,root,root,755)
%{_libdir}/libspdlog.so
%{_includedir}/spdlog
%{_pkgconfigdir}/spdlog.pc
%{_libdir}/cmake/spdlog
