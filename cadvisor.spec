%global debug_package %{nil}
%global user root
%global group root

Name: cadvisor
Version: 0.60.5
Release: 1%{?dist}
Summary: cAdvisor exposes container metrics
License: ASL 2.0
URL:     https://github.com/google/cadvisor

Source0: https://github.com/google/cadvisor/releases/download/v%{version}/%{name}-v%{version}-linux-amd64
Source1: %{name}.unit
Source2: %{name}.default

%{?systemd_requires}
Requires(pre): shadow-utils

%description
cAdvisor (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers.

%prep

%build
/bin/true

%install
mkdir -vp %{buildroot}%{_sharedstatedir}/%{name}
install -D -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%pre
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/default/%{name}
%dir %attr(755, %{user}, %{group}) %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Thu Aug 6 2026 Ivan Garcia <igarcia@cloudox.org> - 0.60.5
- Initial packaging for the 0.60.5 branch
* Tue Mar 31 2026 Ivan Garcia <igarcia@cloudox.org> - 0.56.2
- Initial packaging for the 0.56.2 branch
