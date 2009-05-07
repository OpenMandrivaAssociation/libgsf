%define api_version 1
%define lib_major   114
%define lib_name    %mklibname gsf- %{api_version} %{lib_major}
%define develname    %mklibname -d gsf- %{api_version}

Summary: GNOME Structured File library
Name: libgsf
Version: 1.14.13
Release: %mkrel 1
Epoch: 1
Group: System/Libraries
License: LGPLv2
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: libgsf-1.14.11-format-string.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.gnumeric.org
BuildRequires: libbonobo2_x-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: pygtk2.0-devel
BuildRequires: gtk-doc
BuildRequires: intltool

%description
A library for reading and writing structured files (eg MS OLE and Zip).

%package -n %{lib_name}
Summary:  %{summary}
Group: %{group}

%description -n %{lib_name}
A library for reading and writing structured files (eg MS OLE and Zip).

%package -n %develname
Summary: Support files necessary to compile applications with libgsf
Group: Development/C
Requires: %{lib_name} = %epoch:%{version}
Provides: %{name}-%{api_version}-devel = %epoch:%{version}-%{release}
Provides: %{name}-devel = %epoch:%{version}-%{release}
Requires: libxml2-devel
Requires: libglib2-devel
Obsoletes: %mklibname -d gsf- 1 114

%description -n %develname
Libraries, headers, and support files necessary to compile
applications using libgsf.


%package -n python-libgsf
Summary:  Python bindings for libgsf
Group: Development/Python
Requires: pygtk2.0

%description -n python-libgsf
A library for reading and writing structured files (eg MS OLE and Zip).

%prep

%setup -q
%patch -p1

%build

%configure2_5x --enable-gtk-doc

%make

%install
rm -rf $RPM_BUILD_ROOT libgsf.lang

%makeinstall_std

# remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libgsf
%find_lang libgsf

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{lib_name}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{lib_name}
%endif

%if %mdkversion < 200900
%post
%post_install_gconf_schemas gsf-office-thumbnailer
%endif
 
%preun
%preun_uninstall_gconf_schemas gsf-office-thumbnailer

%files -f libgsf.lang
%defattr(-,root,root)
%doc README
%{_sysconfdir}/gconf/schemas/gsf-office-thumbnailer.schemas
%_bindir/gsf
%_bindir/gsf-vba-dump
%{_bindir}/gsf-office-thumbnailer
%{_mandir}/man1/*

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libgsf*-%{api_version}.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/gsf
%{_libdir}/*.so
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n python-libgsf
%defattr(-,root,root)
%py_platsitedir/gsf/
%py_puresitedir/gsf/

%clean
rm -rf $RPM_BUILD_ROOT


