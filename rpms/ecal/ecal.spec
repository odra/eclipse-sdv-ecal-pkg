%global forgeurl https://github.com/eclipse-ecal/ecal
%global tag v5.11.1
%global debug_package %{nil}

%forgemeta -i

Name:    ecal
Version: 5.11.1
Release: 1%{?dist}
Summary: Eclipse's enhanced Communication Abstraction Layer (eCAL) 
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: g++
BuildRequires: cmake
BuildRequires: protobuf
BuildRequires: protobuf-devel
BuildRequires: asio-devel
BuildRequires: tclap
BuildRequires: simpleini
BuildRequires: spdlog
BuildRequires: spdlog-devel
BuildRequires: gtest
BuildRequires: gtest-devel
BuildRequires: fineftp-server
BuildRequires: tinyxml2
BuildRequires: tinyxml2-devel
BuildRequires: curl-devel
BuildRequires: zlib
BuildRequires: zlib-devel
BuildRequires: libssh2-devel
BuildRequires: hdf5-devel
BuildRequires: termcolor-devel
BuildRequires: recycle
BuildRequires: tcp_pubsub
BuildRequires: qwt-devel

%description
iThe enhanced Communication Abstraction Layer (eCAL) is a middleware that enables scalable, high performance interprocess communication on a single computer node or between different nodes in a computer network. eCAL uses a publish - subscribe pattern to automatically connect different nodes in the network.

%prep
%forgesetup

%build
cmake \
  -DHAS_HDF5=ON \
  -DHAS_QT5=ON \
  -DHAS_CURL=ON \
  -DHAS_CAPNPROTO=ON \
  -DHAS_FTXUI=OFF \
  -DBUILD_DOCS=OFF \
  -DBUILD_APPS=OFF \
  -DBUILD_SAMPLES=OFF \
  -DBUILD_TIME=OFF \
  -DBUILD_PY_BINDING=OFF \
  -DBUILD_STANDALONE_PY_WHEEL=OFF \
  -DBUILD_CSHARP_BINDING=OFF \
  -DBUILD_ECAL_TESTS=ON \
  -DECAL_LAYER_ICEORYX=OFF \
  -DECAL_INCLUDE_PY_SAMPLES=OFF \
  -DECAL_INSTALL_SAMPLE_SOURCES=OFF \
  -DECAL_JOIN_MULTICAST_TWICE=OFF \
  -DECAL_NPCAP_SUPPORT=OFF \
  -DECAL_THIRDPARTY_BUILD_CMAKE_FUNCTIONS=ON \
  -DECAL_THIRDPARTY_BUILD_PROTOBUF=OFF \
  -DECAL_THIRDPARTY_BUILD_SPDLOG=OFF \
  -DECAL_THIRDPARTY_BUILD_TINYXML2=OFF \
  -DECAL_THIRDPARTY_BUILD_FINEFTP=OFF \
  -DECAL_THIRDPARTY_BUILD_CURL=OFF \
  -DECAL_THIRDPARTY_BUILD_GTEST=OFF \
  -DECAL_THIRDPARTY_BUILD_HDF5=OFF \
  -DECAL_THIRDPARTY_BUILD_RECYCLE=OFF \
  -DECAL_THIRDPARTY_BUILD_TCP_PUBSUB=OFF \
  -DECAL_THIRDPARTY_BUILD_QWT=OFF \
  -DECAL_THIRDPARTY_BUILD_YAML-CPP=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_SYSCONFDIR=_etc \
  -DCMAKE_INSTALL_PREFIX=_usr \
  -DCMAKE_INSTALL_LOCALSTATEDIR=_var \
  -DCMAKE_INSTALL_LIBDIR=_lib
make

%install
mkdir -p %{buildroot}%{_includedir}/ecal
mkdir -p %{buildroot}%{_libdir}/cmake/ecal
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
* Mon Jan 17 2023 Leonardo Rossetti <lrossett@redhat.com> - 5.11.1-1
- First version being packaged
