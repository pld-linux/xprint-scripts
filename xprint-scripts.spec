Summary:	Init scripts for Xprint servers
Summary(pl):	Skrypty startowe dla serwerów Xprint
Name:		xprint-scripts
Version:	0.3
Release:	1
License:	GPL
Group:		X11
Source0:	xprintscripts-%{version}.tgz
# Source0-md5:	65ba8e8263e6717e8bfc67545c50aed5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Init scripts for Xprint servers.

%description -l pl
Skrypty startowe dla serwerów Xprint.

%package -n xprint-initrc
Summary:	Init scripts for Xprint servers
Summary(pl):	Skrypty startowe dla serwerów Xprint
Group:		X11
Requires:	xprint-shellscript

%description -n xprint-initrc
Init scripts for Xprint servers.

%description -n xprint-initrc -l pl
Skrypty startowe dla serwerów Xprint.

%package -n xprint-shellscript
Summary:	Init scripts for Xprint servers
Summary(pl):	Skrypt inicjalizuj±cy dla serwerów Xprint
Group:		X11

%description -n xprint-shellscript
Init scripts for Xprint servers.

%description -n xprint-shellscript -l pl
Skrypt inicjalizuj±cy dla serwerów Xprint.

%prep
exit 0

%build
exit 0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

gzip -dc %{SOURCE0} | tar -xf - -C $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n xprint-initrc
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xprint
%dir /etc/sysconfig/Xprint
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/Xprint/*

%files -n xprint-shellscript
%defattr(644,root,root,755)
%attr(755,root,root) /etc/profile.d/*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/xprint
