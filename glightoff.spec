%define	version	1.0.0
%define release	8

Summary:	Simple puzzle game, switch off all the lights on a 5x5 board
Name:		glightoff
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://glightoff.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		glightoff-1.0.0-fix-desktop-file.patch
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
%patch0 -p1

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
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2011.0
+ Revision: 618962
- the mass rebuild of 2010.0 packages

* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 1.0.0-6mdv2010.0
+ Revision: 375619
- fix Licence
- remove redundant desktop file (#49428)
- fix desktop file

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2009.0
+ Revision: 246175
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2008.1
+ Revision: 131568
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import glightoff


* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.0-3mdk
- Fix BuildRequires

* Tue Sep 13 2005 Michael Scherer <misc@mandriva.org> 1.0.0-2mdk
- mkrel
- requires librsvg to be able to load the svg file, fix #18528

* Thu Feb 03 2005 Abel Cheung <deaddog@mandrake.org> 1.0.0-1mdk
- First Mandrake package
