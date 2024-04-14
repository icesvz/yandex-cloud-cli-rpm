Name:           yc
Version:        0.122.0
Release:        1%{?dist}
Summary:        The Yandex Cloud command-line interface CLI

License:        MIT
URL:            https://cloud.yandex.com

Source0:        https://storage.yandexcloud.net/yandexcloud-yc/release/%{version}/linux/amd64/yc

%global         SHA256SUM0 5dd0652aabbb464a34a02f172eec02dbf5bbf4864c55d0b264bb4ede94d1b383

BuildRequires:  curl

%description
The Yandex Cloud command-line interface CLI. 
This is an unofficial package of binary tool provided by Yandex.

%prep
echo 'Prep for %{_arch}'
%ifarch x86_64
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
cd %{_topdir}/BUILD
cp -rf %{_topdir}/SOURCES/yc .
%endif

%install
install -dp %{buildroot}%{_bindir}
install -dp %{buildroot}%{_libdir}/yc
install -dp %{buildroot}%{_libdir}/yc/bin
install -m 755 yc %{buildroot}%{_libdir}/yc/bin
%{__ln_s} -f ../%{_lib}/yc/bin/yc %{buildroot}%{_bindir}/yc

%files
%{_bindir}/yc
%{_libdir}/yc/*

%changelog

* Sun Apr 14 2024 icesvz <icesvz@gmail.com> - 0.122.0
- Bump 

* Wed Apr 03 2024 icesvz <icesvz@gmail.com> - 0.121.0
- Bump 

* Wed Nov 22 2023 icesvz <icesvz@gmail.com> - 0.113.0
- Bump 

* Wed Oct 11 2023 icesvz <icesvz@gmail.com> - 0.110.0
- Bump 

* Wed Aug 23 2023 icesvz <icesvz@gmail.com> - 0.108.1
- Bump 

* Tue Aug 22 2023 icesvz <icesvz@gmail.com> - 0.106.0
- Initial package creation
