Summary:	This client for pbbuttonsd makes some options easy adjustable through a GTK Userinterface.
Summary(pl):	
Name:		powerprefs
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11
Source0:	http://www.cymes.de/members/joker/projects/pbbuttons/tar/%{name}-%{version}.tar.gz
URL:		http://www.cymes.de/members/joker/projects/pbbuttons/powerprefs.html
Requires:	pbbuttonsd
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/pbbuttons
%define		_bindir		%{_sbindir}

%description
This client for pbbuttonsd makes some options easy adjustable through a GTK Userinterface. Following options could directly be 
changed:

    * trackpad mode
      How the trackpad is configured.
    * keyboard mode
      How the keyboard is configured
    * dosleep
      switches sleepmode temporarly off, for eg. long term compiler runs.
    * snoozedelay
      Should the snooze key react immediatly or delayed.
    * ejectdelay
      Should the eject-CD key react immediatly or delayed.
    * mixerdelay
      Should the sound routines be initalized on startup or later.

%description -l pl

%prep
%setup -q

%build
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig},%{_mandir}/man8}

%{__make} install DESTDIR=$RPM_BUILD_ROOT


#gzip -9nf NEWS TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add pbbuttonsd
if [ -f /var/lock/subsys/pbbuttonsd ]; then
	/etc/rc.d/init.d/pbbuttonsd restart >&2
else
	echo "Run \"/etc/rc.d/init.d/pbbuttonsd start\" to start ntp daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/pbbuttonsd ]; then
		/etc/rc.d/init.d/pbbuttonsd stop >&2
	fi
	/sbin/chkconfig --del pbbuttonsd
fi

%files
%defattr(644,root,root,755)
%doc conf/*.gz *.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/ntp
%attr(640,root,root) %config %verify(not size md5 mtime) /etc/sysconfig/*
%{_mandir}/man8/*
