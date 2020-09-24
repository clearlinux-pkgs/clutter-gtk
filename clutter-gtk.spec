#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clutter-gtk
Version  : 1.8.4
Release  : 11
URL      : https://download.gnome.org/sources/clutter-gtk/1.8/clutter-gtk-1.8.4.tar.xz
Source0  : https://download.gnome.org/sources/clutter-gtk/1.8/clutter-gtk-1.8.4.tar.xz
Summary  : GTK+ integration for Clutter
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: clutter-gtk-data = %{version}-%{release}
Requires: clutter-gtk-lib = %{version}-%{release}
Requires: clutter-gtk-license = %{version}-%{release}
Requires: clutter-gtk-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(gtk+-3.0)

%description
Clutter-GTK - GTK+ Integration library for Clutter
-------------------------------------------------------------------------------

%package data
Summary: data components for the clutter-gtk package.
Group: Data

%description data
data components for the clutter-gtk package.


%package dev
Summary: dev components for the clutter-gtk package.
Group: Development
Requires: clutter-gtk-lib = %{version}-%{release}
Requires: clutter-gtk-data = %{version}-%{release}
Provides: clutter-gtk-devel = %{version}-%{release}
Requires: clutter-gtk = %{version}-%{release}

%description dev
dev components for the clutter-gtk package.


%package doc
Summary: doc components for the clutter-gtk package.
Group: Documentation

%description doc
doc components for the clutter-gtk package.


%package lib
Summary: lib components for the clutter-gtk package.
Group: Libraries
Requires: clutter-gtk-data = %{version}-%{release}
Requires: clutter-gtk-license = %{version}-%{release}

%description lib
lib components for the clutter-gtk package.


%package license
Summary: license components for the clutter-gtk package.
Group: Default

%description license
license components for the clutter-gtk package.


%package locales
Summary: locales components for the clutter-gtk package.
Group: Default

%description locales
locales components for the clutter-gtk package.


%prep
%setup -q -n clutter-gtk-1.8.4
cd %{_builddir}/clutter-gtk-1.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586223157
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1586223157
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clutter-gtk
cp %{_builddir}/clutter-gtk-1.8.4/COPYING %{buildroot}/usr/share/package-licenses/clutter-gtk/e60c2e780886f95df9c9ee36992b8edabec00bcc
cp %{_builddir}/clutter-gtk-1.8.4/doc/html/license.html %{buildroot}/usr/share/package-licenses/clutter-gtk/fcc5f7c717e2010765c0563e1d754283d6debab0
%make_install
%find_lang cluttergtk-1.0

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GtkClutter-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/clutter-gtk-1.0/clutter-gtk/clutter-gtk.h
/usr/include/clutter-gtk-1.0/clutter-gtk/gtk-clutter-actor.h
/usr/include/clutter-gtk-1.0/clutter-gtk/gtk-clutter-embed.h
/usr/include/clutter-gtk-1.0/clutter-gtk/gtk-clutter-texture.h
/usr/include/clutter-gtk-1.0/clutter-gtk/gtk-clutter-util.h
/usr/include/clutter-gtk-1.0/clutter-gtk/gtk-clutter-version.h
/usr/include/clutter-gtk-1.0/clutter-gtk/gtk-clutter-window.h
/usr/lib64/libclutter-gtk-1.0.so
/usr/lib64/pkgconfig/clutter-gtk-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/clutter-gtk-1.0/GtkClutterActor.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/GtkClutterEmbed.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/GtkClutterWindow.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/annotation-glossary.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/ch01.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/ch02.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/ch03.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/clutter-gtk-1.0-Utility-Functions.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/clutter-gtk-1.0.devhelp2
/usr/share/gtk-doc/html/clutter-gtk-1.0/cluttergtk-glossary.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/cluttergtk-object-hierarchy.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/cluttergtk-object-index.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/cluttergtk-objects.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/home.png
/usr/share/gtk-doc/html/clutter-gtk-1.0/index.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/ix01.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/ix02.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/left-insensitive.png
/usr/share/gtk-doc/html/clutter-gtk-1.0/left.png
/usr/share/gtk-doc/html/clutter-gtk-1.0/license.html
/usr/share/gtk-doc/html/clutter-gtk-1.0/right-insensitive.png
/usr/share/gtk-doc/html/clutter-gtk-1.0/right.png
/usr/share/gtk-doc/html/clutter-gtk-1.0/style.css
/usr/share/gtk-doc/html/clutter-gtk-1.0/up-insensitive.png
/usr/share/gtk-doc/html/clutter-gtk-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libclutter-gtk-1.0.so.0
/usr/lib64/libclutter-gtk-1.0.so.0.800.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clutter-gtk/e60c2e780886f95df9c9ee36992b8edabec00bcc
/usr/share/package-licenses/clutter-gtk/fcc5f7c717e2010765c0563e1d754283d6debab0

%files locales -f cluttergtk-1.0.lang
%defattr(-,root,root,-)

