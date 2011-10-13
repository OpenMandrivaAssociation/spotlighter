Name:		spotlighter
Summary:	Spotlighter is a tool that show a movable and resizable spotlight on the desktop screen
Version:	0.2
Release:	%mkrel 1
Source0:	http://ardesia.googlecode.com/files/%{name}-%{version}.tar.bz2
URL:		http://code.google.com/p/ardesia
Group:		Education
License:	GPL
BuildRequires:	gcc make automake libtool
BuildRequires:	freetype

Requires:	freetype


%description
Spotlighter is a tool that show a movable and resizable spotlight
on the desktop screen
You can use this to hide and show objects on the desktop
This program has been implemented for educational purposes


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std XDG_UTILS=""
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING NEWS
%{_bindir}/%name
%{_datadir}/%{name}/ui/*.glade
%{_datadir}/%{name}/ui/icons/*
%{_datadir}/icons/%name.xpm
%{_datadir}/icons/%name.ico
%{_datadir}/applications/%name.desktop
%{_datadir}/locale/*
%{_mandir}/man1/%name.*
