%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1
%define major	114
%define libname	%mklibname gsf- %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname	%mklibname -d gsf- %{api}

Summary:	GNOME Structured File library
Name:		libgsf
Epoch:		1
Version:	1.14.25
Release:	3
Group:		System/Libraries
License:	LGPLv2
Url:		http://www.gnumeric.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgsf/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		libgsf-1.14.25-link-python-extension.patch

BuildRequires:	GConf2
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	bzip2-devel
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
BuildRequires:	pkgconfig(pygtk-2.0)

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
%apply_patches
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

