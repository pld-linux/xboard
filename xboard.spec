Summary:	An X Window System graphical chessboard.
Name:		xboard
Version:	4.0.0 
Release:	3
Group:		Amusements/Games
Source:		ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		xboard-header.patch
Patch1:		xboard-4.0.0-xref.patch
Copyright:	GPL
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xboard is an X Window System based graphical chessboard  which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

Install the xboard package if you need a graphical chessboard.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
%configure
make infodir=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	man6dir=$RPM_BUILD_ROOT%{_mandir}/man6 \
	infodir=$RPM_BUILD_ROOT%{_infodir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/* \
	$RPM_BUILD_ROOT%{_infodir}/*

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xboard <<EOF
xboard name "xboard"
xboard description "Chess"
xboard group Games/Strategy
xboard exec "xboard &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%config /etc/X11/wmconfig/xboard
%attr(755,root,root) %{_bindir}/xboard
%attr(755,root,root) %{_bindir}/zic2xpm
%attr(755,root,root) %{_bindir}/cmail
%attr(755,root,root) %{_bindir}/pxboard
%{_mandir}/man6/xboard.6.gz
%{_mandir}/man6/zic2xpm.6.gz
%{_mandir}/man6/cmail.6.gz
%{_infodir}/xboard.info.gz
