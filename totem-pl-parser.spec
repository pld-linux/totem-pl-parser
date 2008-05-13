Summary:	Totem Playlist Parser library
Name:		totem-pl-parser
Version:	2.23.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem-pl-parser/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	88f56d2d3180b6be13890eeb117a700e
URL:		http://www.gnome.org/projects/totem/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 0.61
BuildRequires:	evolution-data-server-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
Provides:	totem-libs
Obsoletes:	totem-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to parse and save playlists, as used in music and movie
players.

%package devel
Summary:	Header files for totem-pl-parser library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki totem-pl-parser
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-vfs2-devel >= 2.22.0
Requires:	gtk+2-devel >= 2:2.12.8
Requires:	libxml2-devel >= 1:2.6.31
Provides:	totem-devel
Obsoletes:	totem-devel

%description devel
Header files for totem-pl-parser library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki totem-pl-parser.

%package static
Summary:	Static totem-pl-parser library
Summary(pl.UTF-8):	Statyczna biblioteka totem-pl-parser
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	totem-static
Obsoletes:	totem-static

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

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv -f po/sr@{Latn,latin}.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtotem-plparser-mini.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtotem-plparser-mini.so.12
%attr(755,root,root) %{_libdir}/libtotem-plparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtotem-plparser.so.12

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser-mini.so
%attr(755,root,root) %{_libdir}/libtotem-plparser.so
%{_libdir}/libtotem-plparser-mini.la
%{_libdir}/libtotem-plparser.la
%{_includedir}/totem-pl-parser
%{_pkgconfigdir}/totem-plparser-mini.pc
%{_pkgconfigdir}/totem-plparser.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtotem-plparser-mini.a
%{_libdir}/libtotem-plparser.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/totem-pl-parser
