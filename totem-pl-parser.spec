Summary:	Totem Playlist Parser library
Summary(pl.UTF-8):	Biblioteka analizująca listy odtwarzania Totema
Name:		totem-pl-parser
Version:	3.10.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem-pl-parser/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	65d403cb4abfc28bdf755914fd3aae7e
Patch0:		ac.patch
URL:		http://www.gnome.org/projects/totem/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gmime-devel >= 2.6.0
BuildRequires:	gnome-common >= 3.5.91
BuildRequires:	gobject-introspection-devel >= 0.9.7
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libarchive-devel >= 2.8.4
BuildRequires:	libgcrypt-devel
BuildRequires:	libquvi-devel >= 0.2.15
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
A library to parse and save playlists, as used in music and movie
players.

%description -l pl.UTF-8
Biblioteka do analizy i zapisu list odtwarzania (playlist) używanych
przez odtwarzacze muzyki i filmów.

%package devel
Summary:	Header files for totem-pl-parser library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki totem-pl-parser
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gmime-devel >= 2.6.0
Requires:	libarchive-devel >= 2.8.4
Requires:	libgcrypt-devel
Requires:	libxml2-devel >= 1:2.6.31
Requires:	quvi-devel >= 0.2.15

%description devel
Header files for totem-pl-parser library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki totem-pl-parser.

%package static
Summary:	Static totem-pl-parser library
Summary(pl.UTF-8):	Statyczna biblioteka totem-pl-parser
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static totem-pl-parser library.

%description static -l pl.UTF-8
Statyczna biblioteka totem-pl-parser.

%package apidocs
Summary:	totem-pl-parser library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki totem-pl-parser
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
totem-pl-parser library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki totem-pl-parser.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtotem-plparser-mini.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtotem-plparser-mini.so.18
%attr(755,root,root) %{_libdir}/libtotem-plparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtotem-plparser.so.18
%{_libdir}/girepository-1.0/TotemPlParser-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser-mini.so
%attr(755,root,root) %{_libdir}/libtotem-plparser.so
%{_includedir}/totem-pl-parser
%{_pkgconfigdir}/totem-plparser-mini.pc
%{_pkgconfigdir}/totem-plparser.pc
%{_datadir}/gir-1.0/TotemPlParser-1.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libtotem-plparser-mini.a
%{_libdir}/libtotem-plparser.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/totem-pl-parser
