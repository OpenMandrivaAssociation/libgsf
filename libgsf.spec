%define api_version 1
%define lib_major   114
%define lib_name	%mklibname gsf- %{api_version} %{lib_major}
%define develname	%mklibname -d gsf- %{api_version}

Summary: GNOME Structured File library
Name: libgsf
Version: 1.14.23
Release: 1
Epoch: 1
Group: System/Libraries
License: LGPLv2
URL: http://www.gnumeric.org
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: GConf2
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.8.0
BuildRequires: pkgconfig(gnome-vfs-2.0) >= 2.2.0
BuildRequires: pkgconfig(gnome-vfs-module-2.0) >= 2.2.0
BuildRequires: pkgconfig(gobject-2.0) >= 2.6.0
BuildRequires: pkgconfig(libbonobo-2.0) >= 2.0.0
BuildRequires: pkgconfig(libxml-2.0) >= 2.4.16
BuildRequires: pkgconfig(popt)
BuildRequires: pkgconfig(pygobject-2.0) >= 2.10.0
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: bzip2-devel

%description
A library for reading and writing structured files (eg MS OLE and Zip).

%package -n %{lib_name}
Summary:  %{summary}
Group: %{group}

%description -n %{lib_name}
A library for reading and writing structured files (eg MS OLE and Zip).

%package -n %{develname}
Summary: Support files necessary to compile applications with libgsf
Group: Development/C
Requires: %{lib_name} = %{epoch}:%{version}-%{release}
Provides: %{name}-%{api_version}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes: %mklibname -d gsf- 1 114

%description -n %{develname}
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

%build

%configure2_5x \
	--disable-static \
	--with-python \
	--enable-gtk-doc

%make

%install
rm -rf %{buildroot} libgsf.lang

%makeinstall_std

# remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/libgsf
rm -f %{buildroot}%{_libdir}/*.la
%find_lang libgsf
#gw put everything in _one_ directory:
%if %_lib != lib
mv %buildroot%{py_puresitedir}/gsf/* %buildroot%{py_platsitedir}/gsf/
%endif


%preun
%preun_uninstall_gconf_schemas gsf-office-thumbnailer

%files -f libgsf.lang
%doc AUTHORS COPYING README
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_bindir}/gsf-office-thumbnailer
%_datadir/thumbnailers/gsf-office.thumbnailer
%{_mandir}/man1/*

%files -n %{lib_name}
%{_libdir}/libgsf*-%{api_version}.so.%{lib_major}*

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/gsf
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n python-libgsf
%{py_platsitedir}/gsf/

