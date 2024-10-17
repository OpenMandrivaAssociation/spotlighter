Name:		spotlighter
Summary:	A tool that show a movable and resizable spotlight on the desktop screen
Version:	0.2
Release:	3
Source0:	http://ardesia.googlecode.com/files/%{name}-%{version}.tar.bz2
URL:		https://code.google.com/p/ardesia
Group:		Education
License:	GPL
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Spotlighter is a tool that show a movable and resizable spotlight
on the desktop screen.
You can use this to hide and show objects on the desktop.
This program has been implemented for educational purposes.


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std XDG_UTILS=""
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/ui/*.glade
%{_datadir}/%{name}/ui/icons/*
%{_datadir}/icons/%{name}.xpm
%{_datadir}/icons/%{name}.ico
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.*

