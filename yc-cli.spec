Name:           yc
Version:        0.106.0
Release:        1%{?dist}
Summary:        The Yandex Cloud command-line interface CLI

License:        MIT
URL:            https://cloud.yandex.com

Source0:        https://storage.yandexcloud.net/yandexcloud-yc/release/%{version}/linux/amd64/yc

%global         SHA256SUM0 03527d1bcbe5ecaee32736ca3080a6016b9df04e52b61d1a0de9c34873c2eeb8

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

* Tue Aug 22 2023 icesvz <icesvz@gmail.com> - 0.106.0
- Initial package creation
