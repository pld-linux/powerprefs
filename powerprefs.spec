Summary:	pbbuttonsd client that allows to adjust some options through a GTK user interface
Summary(pl):	Klient pbbuttonsd pozwalaj±cy zmieniæ niektóre opcje poprzez interfejs w GTK
Name:		powerprefs
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.cymes.de/members/joker/projects/pbbuttons/tar/%{name}-%{version}.tar.gz
# Source0-md5:	f57c9c00ba4417877e1a1504521ef37d
URL:		http://www.cymes.de/members/joker/projects/pbbuttons/powerprefs.html
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	pbbuttonsd-lib
Requires:	pbbuttonsd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:  ppc

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
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}/
