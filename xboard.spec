Summary:	An X Window System graphical chessboard
Summary(pl):	Graficzna szachownica dla X Window
Name:		xboard
Version:	4.0.0
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-header.patch
Patch1:		%{name}-4.0.0-xref.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
Requires:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xboard is an X Window System based graphical chessboard which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

%description -l pl
Xboard to graficzna szachownica pod X Window System, u¿ywana z
programami szachowymi GNUchess i Crafty, serwerami Internet Chess
(ICS), z szachami przez pocztê elektroniczn± itd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure2_13
%{__make} infodir=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/X11/wmconfig,%{_applnkdir}/Games/Board}

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	man6dir=$RPM_BUILD_ROOT%{_mandir}/man6 \
	infodir=$RPM_BUILD_ROOT%{_infodir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Board

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xboard <<EOF
xboard name "xboard"
xboard description "Chess"
xboard group Games/Strategy
xboard exec "xboard &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%config %{_sysconfdir}/X11/wmconfig/xboard
%attr(755,root,root) %{_bindir}/xboard
%attr(755,root,root) %{_bindir}/zic2xpm
%attr(755,root,root) %{_bindir}/cmail
%attr(755,root,root) %{_bindir}/pxboard
%{_applnkdir}/Games/Board/*
%{_mandir}/man6/xboard.6*
%{_mandir}/man6/zic2xpm.6*
%{_mandir}/man6/cmail.6*
%{_infodir}/xboard.info*
