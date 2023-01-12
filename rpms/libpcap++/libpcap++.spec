%global forgeurl https://github.com/seladb/PcapPlusPlus
%global debug_package %{nil}

Version: 22.11

%forgemeta

Name: libpcap++
Release: 1%{?dist}
Summary: a multiplatform C++ library for capturing, parsing and crafting of network packets.
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: gcc-g++
BuildRequires: libpcap-devel
BuildRequires: libstdc++-static

%description
PcapPlusPlus is a multiplatform C++ library for capturing, parsing and crafting of network packets. It is designed to be efficient, powerful and easy to use.

PcapPlusPlus enables decoding and forging capabilities for a large variety of network protocols. It also provides easy to use C++ wrappers for the most popular packet processing engines such as libpcap, WinPcap, Npcap, DPDK and PF_RING.

%prep
%forgeautosetup -p1

%build
install -d ./usr 
./configure-linux.sh \
    --default \
    --install-dir=./usr \
    --libpcap-include-dir=%{_includedir} \
    --libpcap-lib-dir=%{_lib}
make libs

%install
install -d %{buildroot}%{_prefix}/lib
install -d %{buildroot}%{_includedir}
install Dist/libCommon++.a %{buildroot}%{_prefix}/lib/libCommon++.a
install Dist/libPacket++.a %{buildroot}%{_prefix}/lib/libPacket++.a
install Dist/libPcap++.a %{buildroot}%{_prefix}/lib/libPcap++.a
install Dist/header/*.h %{buildroot}%{_includedir}/

%files
%{_prefix}/lib/libCommon++.a
%{_prefix}/lib/libPacket++.a
%{_prefix}/lib/libPcap++.a
%{_includedir}/*.h

%changelog
* Tue Jan 10 2023 Leonardo Rossetti <lrossett@redhat.com> - 22.11-1
- Initial packaging
