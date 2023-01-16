%global forgeurl https://github.com/steinwurf/recycle
%global tag 6.0.0
%global debug_package %{nil}

%forgemeta -i

Name:    recycle
Version: 6.0.0
Release: 1%{?dist}
Summary: Recycle is an implementation of a simple C++ resource pool.
URL:     %{forgeurl}
Source:  %{forgesource}
License: BSD-3-Clause

BuildRequires: g++
BuildRequires: cmake

%description
Recycle is an implementation of a simple C++ resource pool.

%prep
%forgesetup

%build
cmake -DCMAKE_INSTALL_PREFIX=_build

%install
make install
mkdir -p %{buildroot}%{_includedir}/recycle
install _build/include/recycle/no_locking_policy.hpp %{buildroot}%{_includedir}/recycle/no_locking_policy.hpp
install _build/include/recycle/shared_pool.hpp %{buildroot}%{_includedir}/recycle/shared_pool.hpp
install _build/include/recycle/unique_pool.hpp %{buildroot}%{_includedir}/recycle/unique_pool.hpp

%files
%{_includedir}/recycle/no_locking_policy.hpp
%{_includedir}/recycle/shared_pool.hpp
%{_includedir}/recycle/unique_pool.hpp
%license LICENSE.rst
%doc README.rst

%changelog
* Mon Jan 16 2023 Leonardo Rossetti <lrossett@redhat.com> - 6.0.0-1
- First version being packaged
