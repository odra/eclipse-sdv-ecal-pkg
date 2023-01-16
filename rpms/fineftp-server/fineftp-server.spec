%global forgeurl https://github.com/eclipse-ecal/fineftp-server
%global tag v1.3.3
%global debug_package %{nil}

%forgemeta -i

Name:    fineftp-server
Version: 1.3.3
Release: 1%{?dist}
Summary: FineFTP is a minimal FTP server library for Windows and Unix flavors.
URL:     %{forgeurl}
Source:  %{forgesource}
License: BSD-3-Clause

BuildRequires: g++
BuildRequires: cmake
BuildRequires: asio-devel

%description
FineFTP is a minimal FTP server library for Windows and Unix flavors. The project is CMake based and only depends on asio, which is integrated as git submodule. No boost is required.

You can easily embed this library into your own project in order to create an embedded FTP Server. It was developed and tested on Windows 10 (Visual Studio 2015 / 2019, MinGW) and Ubuntu 16.04 - 21.10 (gcc 5.4.0 - 11.2.0).

%prep
%forgesetup

%build
cd fineftp-server
cmake .. \
-D asio_INCLUDE_DIR=%{_includedir}/asio \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_INSTALL_PREFIX=_build
make

%install
mkdir -p %{buildroot}%{_includedir}/fineftp
mkdir -p %{buildroot}%{_libdir}/cmake/fineftp
cd fineftp-server
make install
# headers
install _build/include/fineftp/fineftp_export.h %{buildroot}%{_includedir}/fineftp/
install _build/include/fineftp/fineftp_version.h %{buildroot}%{_includedir}/fineftp/
install _build/include/fineftp/permissions.h %{buildroot}%{_includedir}/fineftp/
install _build/include/fineftp/server.h %{buildroot}%{_includedir}/fineftp/
# lib
install _build/lib/libfineftp-server.a %{buildroot}%{_libdir}/
install _build/lib/cmake/fineftp/fineftpConfig.cmake %{buildroot}%{_libdir}/cmake/fineftp/
install _build/lib/cmake/fineftp/fineftpTargets.cmake %{buildroot}%{_libdir}/cmake/fineftp/
install _build/lib/cmake/fineftp/fineftpTargets-release.cmake %{buildroot}%{_libdir}/cmake/fineftp/

%files
# headers
%{_includedir}/fineftp/fineftp_export.h
%{_includedir}/fineftp/fineftp_version.h
%{_includedir}/fineftp/permissions.h
%{_includedir}/fineftp/server.h
# libs
%{_libdir}/libfineftp-server.a
%{_libdir}/cmake/fineftp/fineftpConfig.cmake
%{_libdir}/cmake/fineftp/fineftpTargets.cmake
%{_libdir}/cmake/fineftp/fineftpTargets-release.cmake
# license and docs
%license LICENSE
%doc README.md

%changelog
* Mon Jan 16 2023 Leonardo Rossetti <lrossett@redhat.com> - 1.3.3-1
- First version being packaged
