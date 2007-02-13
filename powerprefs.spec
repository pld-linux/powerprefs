Summary:	pbbuttonsd client that allows to adjust some options through a GTK+ user interface
Summary(pl.UTF-8):	Klient pbbuttonsd pozwalający zmienić niektóre opcje poprzez interfejs w GTK+
Name:		powerprefs
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pbbuttons/%{name}-%{version}.tar.gz
# Source0-md5:	d29c1aa01e4f47281abe7c8b921c591d
URL:		http://pbbuttons.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
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

%description -l pl.UTF-8
Ten klient pbbuttonsd pozwala łatwo zmienić niektóre opcje poprzez
interfejs użytkownika oparty na GTK+. Można ustalić:
- tryb trackpada
- tryb klawiatury
- czy komputer ma wchodzić w tryb uśpienia
- czy usypanie przyciskiem ma być natychmiastowe, czy z opóźnieniem
- czy wysuwanie CD ma być natychmiastowe, czy z opóźnieniem
- czy dźwięk ma być inicjalizowany natychmiast po starcie, czy później.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
