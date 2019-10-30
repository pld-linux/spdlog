Summary:	Very fast C++ logging library
Summary(pl.UTF-8):	Bardzo szybka biblioteka C++ do logowania
Name:		spdlog
Version:	0.16.1
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/COMBINE-lab/spdlog/releases
Source0:	https://github.com/COMBINE-lab/spdlog/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5fc7dcdd9363b38b53e4705f5da9ca17
URL:		https://github.com/COMBINE-lab/spdlog
BuildRequires:	cmake >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very fast, header only, C++ logging library. 

%description -l pl.UTF-8
Bardzo szybka, składająca się z samych nagłówków biblioteka C++ do
logowania.

%package devel
Summary:	Very fast C++ logging library
Summary(pl.UTF-8):	Bardzo szybka biblioteka C++ do logowania
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7

%description devel
Very fast, header only, C++ logging library. 

%description devel -l pl.UTF-8
Bardzo szybka, składająca się z samych nagłówków biblioteka C++ do
logowania.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DBUILD_TESTING=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/spdlog
%{_pkgconfigdir}/spdlog.pc
%{_libdir}/cmake/spdlog
