%define	version	1.0.0
%define release	%mkrel 5

Summary:	Simple puzzle game, switch off all the lights on a 5x5 board
Name:		glightoff
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Puzzles
URL:		http://glightoff.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk2-devel >= 2.6
BuildRequires:	imagemagick
BuildRequires:  perl-XML-Parser
# see bug 18528, 
Requires:       librsvg

%description
GLightOff is a simple (but not so easy to solve!) puzzle game.
The goal is to switch off all the lights on the 5x5 board.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# icons
mkdir -p %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
install -D -m 644       glightoff.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 glightoff.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 glightoff.png %{buildroot}%{_miconsdir}/%{name}.png

# menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name} 
Icon=%{name} 
Comment=Switch all lights off in game board 
Categories=Game;LogicGame; 
Name=GLightOff
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

