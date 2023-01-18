%global forgeurl https://github.com/brofield/simpleini

Version: 4.19

%forgemeta

Name: simpleini
Release: 1%{?dist}
Summary: Read and write INI-style configuration files.
URL:     %{forgeurl}
Source:  %{forgesource}
License: MIT

BuildRequires: gcc
BuildRequires: g++
BuildRequires: pkgconf-pkg-config
BuildRequires: gtest
BuildRequires: gtest-devel

%description
A cross-platform library that provides a simple API to read and write INI-style configuration files. It supports data files in ASCII, MBCS and Unicode. It is designed explicitly to be portable to any platform and has been tested
on Windows, WinCE and Linux. Released as open-source and free using the MIT licence.

%prep
%forgesetup

%build
gcc -g -Wall -shared -o libsimpleini.so -fPIC ConvertUTF.c

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
install -C -m 644 SimpleIni.h %{buildroot}%{_includedir}/SimpleIni.h
install -C -m 644 ConvertUTF.h %{buildroot}%{_includedir}/ConvertUTF.h
install libsimpleini.so %{buildroot}%{_libdir}/libsimpleini.so

%check
cd tests
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-roundtrip.o ts-roundtrip.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-snippets.o ts-snippets.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-utf8.o ts-utf8.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-bugfix.o ts-bugfix.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-quotes.o ts-quotes.cpp
g++ -Wall -std=c++11 `pkg-config --cflags gtest_main` -c -o ts-noconvert.o ts-noconvert.cpp
g++ -o ./tests ts-roundtrip.o ts-snippets.o ts-utf8.o ts-bugfix.o ts-quotes.o ts-noconvert.o `pkg-config --libs gtest_main`
./tests

%files
%{_includedir}/SimpleIni.h
%{_includedir}/ConvertUTF.h
%{_libdir}/libsimpleini.so
%license LICENCE.txt
%doc README.md

%changelog
* Mon Dec 05 2022 Leonardo Rossetti <lrossett@redhat.com> - 0.0.1
- First version being packaged
