%define	version	1.0.0
%define release	%mkrel 3

Summary:	Simple puzzle game, switch off all the lights on a 5x5 board
Name:		glightoff
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Puzzles
URL:		http://glightoff.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel >= 2.6
BuildRequires:	ImageMagick
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
mkdir -p %{buildroot}%{_menudir}
cat << _EOF_ > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
 command="%{_bindir}/%{name}" \
 icon="%{name}.png" \
 longtitle="Switch all lights off in game board" \
 needs="x11" \
 section="More Applications/Games/Puzzles" \
 title="GLightOff"
_EOF_

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

