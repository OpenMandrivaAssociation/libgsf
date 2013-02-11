%define api	1
%define major	114
%define libname	%mklibname gsf- %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname	%mklibname -d gsf- %{api}


Summary:	GNOME Structured File library
Name:		libgsf
Epoch:		1
Version:	1.14.25
Release:	1
Group:		System/Libraries
License:	LGPLv2
URL:		http://www.gnumeric.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/1.14/%{name}-%{version}.tar.xz
Patch0:		libgsf-1.14.25-link-python-extension.patch

BuildRequires:	GConf2
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	bzip2-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.8.0
BuildRequires:	pkgconfig(gnome-vfs-2.0) >= 2.2.0
BuildRequires:	pkgconfig(gnome-vfs-module-2.0) >= 2.2.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.6.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.4
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0 
BuildRequires:	pkgconfig(libbonobo-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.16
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(pygobject-2.0)

%description
A library for reading and writing structured files (eg MS OLE and Zip).

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
A library for reading and writing structured files (eg MS OLE and Zip).

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Support files necessary to compile applications with libgsf
Group:		Development/C
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Requires:	%{girname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-%{api}-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	%mklibname -d gsf- 1 114

%description -n %{devname}
Libraries, headers, and support files necessary to compile
applications using libgsf.

%package -n python-libgsf
Summary:	Python bindings for libgsf
Group:		Development/Python
Requires:	pygtk2.0

%description -n python-libgsf
A library for reading and writing structured files (eg MS OLE and Zip).

%prep
%setup -q
%patch0 -p1 -b .pylink~
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--with-python \
	--enable-gtk-doc \
	--enable-introspection

%make

%install
%makeinstall_std

# remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/libgsf

#gw put everything in _one_ directory:
%if %{_lib} != lib
mv %{buildroot}%{py_puresitedir}/gsf/* %{buildroot}%{py_platsitedir}/gsf/
%endif

%find_lang libgsf

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_bindir}/gsf-office-thumbnailer
%{_datadir}/thumbnailers/gsf-office.thumbnailer
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libgsf*-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gsf-%{api}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/gsf
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*.gir

%files -n python-libgsf
%{py_platsitedir}/gsf/


%changelog
* Thu May 31 2012 Guilherme Moro <guilherme@mandriva.com> 1:1.14.23-3
+ Revision: 801462
- Enable typelib

* Fri Apr 20 2012 Götz Waschk <waschk@mandriva.org> 1:1.14.23-2
+ Revision: 792398
- bump release
- fix python module installation
- enable python and bzip2 support
- update to new version 1.14.23

* Fri Dec 16 2011 Götz Waschk <waschk@mandriva.org> 1:1.14.22-1
+ Revision: 741711
- update file list
- new version
- xz tarball

* Sat Nov 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:1.14.21-2
+ Revision: 733497
- fixed BRs
- rebuild
- cleaned up spec
- removed clean section
- removed defattr
- removed .la files
- disabled static build
- removed old post/un scriptlets
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot

* Fri May 20 2011 Götz Waschk <waschk@mandriva.org> 1:1.14.21-1
+ Revision: 676367
- new version

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.14.20-2
+ Revision: 662373
- mass rebuild

* Fri Mar 25 2011 Götz Waschk <waschk@mandriva.org> 1:1.14.20-1
+ Revision: 648475
- new version
- drop patch

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 1:1.14.19-2mdv2011.0
+ Revision: 593335
- rebuild for new python 2.7

* Sat Sep 25 2010 Götz Waschk <waschk@mandriva.org> 1:1.14.19-1mdv2011.0
+ Revision: 581037
- update to new version 1.14.19

* Thu Apr 08 2010 Götz Waschk <waschk@mandriva.org> 1:1.14.18-1mdv2010.1
+ Revision: 532883
- update build deps
- update to new version 1.14.18

* Sun Feb 14 2010 Götz Waschk <waschk@mandriva.org> 1:1.14.17-1mdv2010.1
+ Revision: 505611
- update to new version 1.14.17

* Mon Oct 12 2009 Götz Waschk <waschk@mandriva.org> 1:1.14.16-1mdv2010.0
+ Revision: 456724
- update to new version 1.14.16

* Sat Jun 20 2009 Götz Waschk <waschk@mandriva.org> 1:1.14.15-1mdv2010.0
+ Revision: 387478
- update to new version 1.14.15

* Sun May 24 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.14.14-1mdv2010.0
+ Revision: 379148
- update to new version 1.14.14

* Thu May 07 2009 Götz Waschk <waschk@mandriva.org> 1:1.14.13-1mdv2010.0
+ Revision: 372796
- update to new version 1.14.13

* Mon Apr 27 2009 Götz Waschk <waschk@mandriva.org> 1:1.14.12-1mdv2010.0
+ Revision: 369049
- update to new version 1.14.12

* Wed Jan 07 2009 Götz Waschk <waschk@mandriva.org> 1:1.14.11-1mdv2009.1
+ Revision: 326458
- new version
- fix format string

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 1:1.14.10-2mdv2009.1
+ Revision: 319682
- use makeinstall_std
- rebuild for new python

* Sun Oct 19 2008 Götz Waschk <waschk@mandriva.org> 1:1.14.10-1mdv2009.1
+ Revision: 295261
- update to new version 1.14.10

* Sun Aug 31 2008 Götz Waschk <waschk@mandriva.org> 1:1.14.9-1mdv2009.0
+ Revision: 277781
- new version
- update license
- update build deps

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 1:1.14.8-3mdv2009.0
+ Revision: 227421
- rebuild for fixed %%update_icon_cache/%%clean_icon_cache/%%post_install_gconf_schemas
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1:1.14.8-2mdv2009.0
+ Revision: 222878
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Mar 06 2008 Götz Waschk <waschk@mandriva.org> 1:1.14.8-1mdv2008.1
+ Revision: 180316
- new version

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1:1.14.7-2mdv2008.1
+ Revision: 150687
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Sep 07 2007 Götz Waschk <waschk@mandriva.org> 1:1.14.7-1mdv2008.0
+ Revision: 81960
- new version
- new devel name

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 1:1.14.6-1mdv2008.0
+ Revision: 79219
- new version

* Wed Jul 11 2007 Götz Waschk <waschk@mandriva.org> 1:1.14.5-1mdv2008.0
+ Revision: 51224
- new version
- fix build

* Mon Jun 18 2007 Götz Waschk <waschk@mandriva.org> 1:1.14.4-1mdv2008.0
+ Revision: 40841
- new version


* Mon Nov 06 2006 Götz Waschk <waschk@mandriva.org> 1.14.3-1mdv2007.0
+ Revision: 77034
- new version

* Sun Oct 15 2006 Götz Waschk <waschk@mandriva.org> 1:1.14.2-3mdv2007.1
+ Revision: 64780
- fix file list for x86_64
- rebuild
- Import libgsf

* Thu Oct 05 2006 G�tz Waschk <waschk@mandriva.org> 1.14.2-1mdv2007.0
- add python package
- New version 1.14.2

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1:1.14.1-2mdv2007.0
- Rebuild with latest dbus

* Tue May 09 2006 Götz Waschk <waschk@mandriva.org> 1:1.14.1-1mdk
- New release 1.14.1

* Thu Mar 02 2006 G�tz Waschk <waschk@mandriva.org> 1.14.0-1mdk
- new major
- New release 1.14.0

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 1:1.13.3-3mdk
- Fix schema install/uninstall (copy/paste is bad sometimes ;)

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 1:1.13.3-2mdk
- Use mkrel

* Mon Nov 07 2005 Götz Waschk <waschk@mandriva.org> 1.13.3-1mdk
- New release 1.13.3

* Wed Oct 12 2005 G�tz Waschk <waschk@mandriva.org> 1.13.2-2mdk
- fix major

* Wed Oct 12 2005 Götz Waschk <waschk@mandriva.org> 1.13.2-1mdk
- New release 1.13.2

* Fri Oct 07 2005 Frederic Crozat <fcrozat@mandriva.com> 1.12.3-1mdk
- Release 1.12.3

* Thu Aug 18 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.12.2-2mdk
- add BuildRequires: perl-XML-Parser

* Wed Aug 17 2005 G�tz Waschk <waschk@mandriva.org> 1.12.2-1mdk
- update file list
- enable gtk-doc
- New release 1.12.2

* Sat Jul 30 2005 Frederic Crozat <fcrozat@mandriva.com> 1.12.1-1mdk 
- Switch back to 1.12.1

* Thu Jun 09 2005 G�tz Waschk <waschk@mandriva.org> 1:1.11.1-1mdk
- back to 1.11.1

* Wed May 11 2005 G�tz Waschk <waschk@mandriva.org> 1.12.0-1mdk
- New release 1.12.0

* Fri Jan 21 2005 Goetz Waschk <waschk@linux-mandrake.com> 1.11.1-1mdk
- New release 1.11.1

* Tue Aug 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.10.1-1mdk
- New release 1.10.1

* Tue Jul 06 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.10.0-1mdk
- reenable libtooliz
- New release 1.10.0

* Tue May 18 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.9.1-1mdk
- fix gtk-doc location
- drop patch
- New release 1.9.1

* Thu May 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.9.0-1mdk
- New release 1.9.0

