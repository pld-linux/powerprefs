Summary:	pbbuttonsd client that allows to adjust some options through a GTK+ user interface
Summary(pl):	Klient pbbuttonsd pozwalaj�cy zmieni� niekt�re opcje poprzez interfejs w GTK+
Name:		powerprefs
Version:	0.4.6
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pbbuttons/%{name}-%{version}.tar.gz
# Source0-md5:	6eddd3f35d3f89bf01549093995dbf90
URL:		http://pbbuttons.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	pbbuttonsd-lib
Requires:	pbbuttonsd
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client for pbbuttonsd makes some options easy adjustable through
a GTK+ user interface. Following options could directly be changed:
- trackpad mode
  How the trackpad is configured.
- keyboard mode
  How the keyboard is configured.
- dosleep
  switches sleepmode temporarly off, for eg. long term compiler runs.
- snoozedelay
  Should the snooze key react immediatly or delayed.
- ejectdelay
  Should the eject-CD key react immediatly or delayed.
- mixerdelay
  Should the sound routines be initalized on startup or later.

%description -l pl
Ten klient pbbuttonsd pozwala �atwo zmieni� niekt�re opcje poprzez
interfejs u�ytkownika oparty na GTK+. Mo�na ustali�:
- tryb trackpada
- tryb klawiatury
- czy komputer ma wchodzi� w tryb u�pienia
- czy usypanie przyciskiem ma by� natychmiastowe, czy z op�nieniem
- czy wysuwanie CD ma by� natychmiastowe, czy z op�nieniem
- czy d�wi�k ma by� inicjalizowany natychmiast po starcie, czy p�niej.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
