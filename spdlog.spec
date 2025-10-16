Summary:	Very fast C++ logging library
Summary(pl.UTF-8):	Bardzo szybka biblioteka C++ do logowania
Name:		spdlog
Version:	1.15.3
Release:	1
Epoch:		1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/gabime/spdlog/releases
Source0:	https://github.com/gabime/spdlog/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fffda902bb4a04ce814ddd5328d95e8a
URL:		https://github.com/gabime/spdlog
BuildRequires:	cmake >= 3.10
BuildRequires:	libfmt-devel >= 5.3.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libfmt >= 5.3.0
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
Requires:	libstdc++-devel >= 6:4.7

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
	-DSPDLOG_FMT_EXTERNAL=ON

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
%ghost %{_libdir}/libspdlog.so.1.15

%files devel
%defattr(644,root,root,755)
%{_libdir}/libspdlog.so
%{_includedir}/spdlog
%{_pkgconfigdir}/spdlog.pc
%{_libdir}/cmake/spdlog
