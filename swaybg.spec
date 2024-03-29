#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swaybg
Version  : 1.2.0
Release  : 7
URL      : https://github.com/swaywm/swaybg/archive/v1.2.0/swaybg-1.2.0.tar.gz
Source0  : https://github.com/swaywm/swaybg/archive/v1.2.0/swaybg-1.2.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: swaybg-bin = %{version}-%{release}
Requires: swaybg-license = %{version}-%{release}
Requires: swaybg-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : scdoc

%description
# swaybg
swaybg is a wallpaper utility for Wayland compositors. It is compatible with
any Wayland compositor which implements the wlr-layer-shell protocol and
`wl_output` version 4.

%package bin
Summary: bin components for the swaybg package.
Group: Binaries
Requires: swaybg-license = %{version}-%{release}

%description bin
bin components for the swaybg package.


%package license
Summary: license components for the swaybg package.
Group: Default

%description license
license components for the swaybg package.


%package man
Summary: man components for the swaybg package.
Group: Default

%description man
man components for the swaybg package.


%prep
%setup -q -n swaybg-1.2.0
cd %{_builddir}/swaybg-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670508028
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/swaybg
cp %{_builddir}/swaybg-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/swaybg/841449f83a67bf0e5197b94f9b9b61eb3ff097e0 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swaybg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swaybg/841449f83a67bf0e5197b94f9b9b61eb3ff097e0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swaybg.1
