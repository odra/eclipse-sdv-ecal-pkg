%global forgeurl https://github.com/odra/tcp_pubsub
%global branch master
%global debug_package %{nil}

%forgemeta -i

Name:    tcp_pubsub
Version: 1.0.3
Release: 1%{?dist}
Summary: A minimal publish-subscribe library that transports data via TCP
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: g++
BuildRequires: cmake
BuildRequires: asio-devel
BuildRequires: recycle
BuildRequires: tree

%description
tcp_pubsub is a minimal publish-subscribe library that transports data via TCP. The project is CMake based. The dependencies are integrated as git submodules. In your own Project you can either use those submodules as well, or provide the dependencies in your own manner.

tcp_pubsub does not define a message format but only transports binary blobs. It does however define a protocol around that, which is kept as lightweight as possible.

%prep
%forgesetup

%build
cmake \
-D asio_INCLUDE_DIR=%{_includedir}/asio \
-D recycle_INCLUDE_DIR=%{_includedir}/recycle \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_INSTALL_PREFIX=_build
make

%install
mkdir -p %{buildroot}%{_includedir}/tcp_pubsub
mkdir -p %{buildroot}%{_libdir}/cmake/tcp_pubsub
make install
# headers
install _build/include/tcp_pubsub/callback_data.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/executor.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/publisher.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/subscriber.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/subscriber_session.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/tcp_pubsub_export.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/tcp_pubsub_logger.h %{buildroot}%{_includedir}/tcp_pubsub/
install _build/include/tcp_pubsub/tcp_pubsub_version.h %{buildroot}%{_includedir}/tcp_pubsub/
# lib
tree _build/
install _build/lib/libtcp_pubsub.a %{buildroot}%{_libdir}/libtcp_pubsub.a
install _build/lib/cmake/tcp_pubsub/tcp_pubsubConfig.cmake %{buildroot}%{_libdir}/cmake/tcp_pubsub/
install _build/lib/cmake/tcp_pubsub/tcp_pubsubTargets.cmake %{buildroot}%{_libdir}/cmake/tcp_pubsub/

%files
# headers
%{_includedir}/tcp_pubsub/callback_data.h
%{_includedir}/tcp_pubsub/executor.h
%{_includedir}/tcp_pubsub/publisher.h
%{_includedir}/tcp_pubsub/subscriber.h
%{_includedir}/tcp_pubsub/subscriber_session.h
%{_includedir}/tcp_pubsub/tcp_pubsub_export.h
%{_includedir}/tcp_pubsub/tcp_pubsub_logger.h
%{_includedir}/tcp_pubsub/tcp_pubsub_version.h
# libs
%{_libdir}/libtcp_pubsub.a
%{_libdir}/cmake/tcp_pubsub/tcp_pubsubConfig.cmake
%{_libdir}/cmake/tcp_pubsub/tcp_pubsubTargets.cmake
# license and docs
%license LICENSE
%doc README.md

%changelog
* Mon Jan 16 2023 Leonardo Rossetti <lrossett@redhat.com> - 1.0.3-1
- First version being packaged
