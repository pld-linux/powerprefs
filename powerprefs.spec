Summary:	pbbuttonsd client that allows to adjust some options through a GTK user interface
Summary(pl):	Klient pbbuttonsd pozwalaj±cy zmieniæ niektóre opcje poprzez interfejs w GTK
Name:		powerprefs
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.cymes.de/members/joker/projects/pbbuttons/tar/%{name}-%{version}.tar.gz
URL:		http://www.cymes.de/members/joker/projects/pbbuttons/powerprefs.html
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
Requires:	pbbuttonsd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/pbbuttons
%define		_bindir		%{_sbindir}

%description
This client for pbbuttonsd makes some options easy adjustable through
a GTK user interface. Following options could directly be changed:
 * trackpad mode
   How the trackpad is configured.
 * keyboard mode
   How the keyboard is configured.
 * dosleep
   switches sleepmode temporarly off, for eg. long term compiler runs.
 * snoozedelay
   Should the snooze key react immediatly or delayed.
 * ejectdelay
   Should the eject-CD key react immediatly or delayed.
 * mixerdelay
   Should the sound routines be initalized on startup or later.

%description -l pl
Ten klient pbbuttonsd pozwala ³atwo zmieniæ niektóre opcje poprzez
interfejs u¿ytkownika oparty na GTK. Mo¿na ustaliæ:
- tryb trackpada
- tryb klawiatury
- czy komputer ma wchodziæ w tryb u¶pienia
- czy usypanie przyciskiem ma byæ natychmiastowe, czy z opó¼nieniem
- czy wysuwanie CD ma byæ natychmiastowe, czy z opó¼nieniem
- czy d¼wiêk ma byæ inicjalizowany natychmiast po starcie, czy pó¼niej.

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

%files
%defattr(644,root,root,755)
%doc conf/*.gz *.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config %verify(not size md5 mtime) /etc/sysconfig/*
%{_mandir}/man8/*
