%global forgeurl https://github.com/seladb/PcapPlusPlus

Version: 22.11

%forgemeta

Name: libpcap++
Release: 1%{?dist}
Summary: a multiplatform C++ library for capturing, parsing and crafting of network packets.
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: g++
BuildRequires: libpcap-devel

%description
PcapPlusPlus is a multiplatform C++ library for capturing, parsing and crafting of network packets. It is designed to be efficient, powerful and easy to use.

PcapPlusPlus enables decoding and forging capabilities for a large variety of network protocols. It also provides easy to use C++ wrappers for the most popular packet processing engines such as libpcap, WinPcap, Npcap, DPDK and PF_RING.

%prep
%forgesetup

%build
./configure-linux --default
make

%check
cd Tests/Packet++Test/
./Bin/Packet++Test

%install
%make_install

%files
%license LICENCE
%doc README.md

%changelog
* Mon Dec 06 2022 Leonardo Rossetti <lrossett@redhat.com> - 0.0.1
- First version being packaged
