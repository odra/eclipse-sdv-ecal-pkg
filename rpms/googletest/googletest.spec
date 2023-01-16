%global forgeurl https://github.com/google/googletest.git
%global debug_package %{nil}

Version: 1.12.1

%forgemeta

Name: googletest
Release: 1%{?dist}
Summary: GoogleTest is Google's C++ testing and mocking framework.
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: gcc-g++

%description
Google c++ testing framework.

%prep
%forgeautosetup -p1

%build
install -d %{buildroot}%{_prefix}
cmake \
-DCMAKE_CXX_STANDARD=14 \
-Dgtest_build_samples=ON \
-Dgtest_build_tests=ON \
-Dgmock_build_tests=ON \
-Dcxx_no_exception=OFF \
-Dcxx_no_rtti=OFF \
-DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix}
make

%install
make install

%files
%dir %{buildroot}%{_includedir}
%dir %{buildroot}%{_prefix}/%{_lib}

%changelog
* Tue Jan 16 2023 Leonardo Rossetti <lrossett@redhat.com> - 1.12.1-1
- Initial packaging
