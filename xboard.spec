Summary: An X Window System graphical chessboard.
Name: xboard
Version: 4.0.0 
Release: 3
Group: Amusements/Games
Source: ftp://ftp.gnu.org/pub/gnu/xboard-4.0.0.tar.gz
Patch0: xboard-header.patch
Patch1: xboard-4.0.0-xref.patch
Copyright: GPL
BuildRoot: /var/tmp/xboard-root

%description
Xboard is an X Window System based graphical chessboard  which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

Install the xboard package if you need a graphical chessboard.

%prep
%setup -q 
%patch0 -p1 -b .orig
%patch1 -p1

%build
./configure --prefix=/usr
make

%install
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/xboard

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xboard <<EOF
xboard name "xboard"
xboard description "Chess"
xboard group Games/Strategy
xboard exec "xboard &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/xboard
/usr/bin/zic2xpm
/usr/bin/cmail
/usr/bin/pxboard
/usr/man/man6/xboard.6
/usr/man/man6/zic2xpm.6
/usr/man/man6/cmail.6
/usr/info/xboard.info
%config /etc/X11/wmconfig/xboard
