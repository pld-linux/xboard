Summary:	An X Window System graphical chessboard
Summary(de):	X11-Schnittstelle für GNU-Schach
Summary(es):	Interface X11 para el ajedrez de la GNU
Summary(fr):	Interface X11 au jeu d'échecs de GNU
Summary(pl):	Graficzna szachownica dla X Window
Summary(pt_BR):	Interface X11 para o xadrez da GNU
Summary(ru):	çÒÁÆÉÞÅÓËÉÊ (X11) ÉÎÔÅÒÆÅÊÓ Ë ÛÁÈÍÁÔÎÙÍ ÐÒÏÇÒÁÍÍÁÍ
Summary(tr):	GNU Chess (satranç) oyununa X11 grafik arabirimi
Summary(uk):	çÒÁÆ¦ÞÎÉÊ (X11) ¦ÎÔÅÒÆÅÊÓ ÄÏ ÛÁÈÏ×ÉÈ ÐÒÏÇÒÁÍ
Name:		xboard
Version:	4.2.7
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.gnu.org/gnu/xboard/%{name}-%{version}.tar.gz
# Source0-md5:	b70ad8ff7569975302c5fb402d5eea32
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
URL:		http://www.tim-mann.org/xboard.html
BuildRequires:	automake
BuildRequires:	texinfo
Requires:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xboard is an X Window System based graphical chessboard which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

%description -l de
xboard stellt eine einfach zu bedienende, grafische Oberfläche für
GNU-Schach bereit, so daß Sie sich in stundenlange Schachkämpfe
verwickeln können, ohne komplizierte Befehle lernen zu müssen.Es läßt
sich auch als Frontend zum Austragen von Schachpartien gegen andere
Internet-Benutzer einsetzen.

%description -l es
xboard te ofrece una interface gráfica fácil de usar para el programa
de ajedrez de GNU, permitiendo que aproveches horas de la ación
intelectual sin tener que aprender comandos complicados.

%description -l fr
xboard vous offre une interface graphique facile à utiliser pour le
jeu d'échecs de GNU. Il vous permet d'apprécier les heures de
réflexion des échecs sans avoir à apprendre des commandes complexes.
Il peut aussi être utilisé comme frontal pour jouer aux échecs avec
d'autres personnes sur l'Internet.

%description -l pl
Xboard to graficzna szachownica pod X Window System, u¿ywana z
programami szachowymi GNUchess i Crafty, serwerami Internet Chess
(ICS), z szachami przez pocztê elektroniczn± itd.

%description -l pt_BR
xboard oferece a você uma interface gráfica fácil de usar para o
programa de xadrez da GNU, permitindo você aproveitar horas da ação
intelectual sem ter que aprender comandos complicados.

%description -l ru
Xboard - ÜÔÏ ÇÒÁÆÉÞÅÓËÉÊ ÉÎÔÅÒÆÅÊÓ Ë ÛÁÈÍÁÔÎÙÍ ÐÒÏÇÒÁÍÍÁÍ, ËÏÔÏÒÙÊ
ÍÏÖÅÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎ Ó ÐÒÏÇÒÁÍÍÁÍÉ GNUchess É Crafty, Ó ÛÁÈÍÁÔÎÙÍÉ
ÓÅÒ×ÅÒÁÍÉ × éÎÔÅÒÎÅÔÅ (ICS), Ó ÛÁÈÍÁÔÁÍÉ ÐÏ ÜÌÅËÔÒÏÎÎÏÊ ÐÏÞÔÅ ÉÌÉ Ó
ÓÏÈÒÁÎÅÎÎÙÍÉ ÚÁÐÉÓÑÍÉ ÉÇÒ.

%description -l tr
xboard, GNU chess programýna grafik arabirimi ekleyerek kullanýmý
kolay ve rahat bir ortam sunar. Saatler boyunca kafa yorabilirsiniz.
Internet üzerinden arkadaþýnýzla da oynayabilirsiniz.

%description -l uk
Xboard - ÃÅ ÇÒÁÆ¦ÞÎÉÊ ¦ÎÔÅÒÆÅÊÓ ÄÏ ÛÁÈÏ×ÉÈ ÐÒÏÇÒÁÍ, ÑËÉÊ ÍÏÖÅ ÂÕÔÉ
×ÉËÏÒÉÓÔÁÎÉÊ Ú ÐÒÏÇÒÁÍÁÍÉ GNUchess ÔÁ Crafty, Ú ÛÁÈÏ×ÉÍÉ ÓÅÒ×ÅÒÁÍÉ ×
¶ÎÔÅÒÎÅÔ¦ (ICS), Ú ÛÁÈÁÍÉ ÐÏ ÅÌÅËÔÒÏÎÎ¦Ê ÐÏÛÔ¦ ÞÉ ¦Ú ÚÂÅÒÅÖÅÎÉÍÉ
ÚÁÐÉÓÁÍÉ ¦ÇÏÒ.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	man6dir=$RPM_BUILD_ROOT%{_mandir}/man6 \
	infodir=$RPM_BUILD_ROOT%{_infodir}

echo '.so xboard.6' > $RPM_BUILD_ROOT%{_mandir}/man6/cmail.6
echo '.so xboard.6' > $RPM_BUILD_ROOT%{_mandir}/man6/pxboard.6

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cmail
%attr(755,root,root) %{_bindir}/pxboard
%attr(755,root,root) %{_bindir}/xboard
%attr(755,root,root) %{_bindir}/zic2xpm
%{_mandir}/man6/cmail.6*
%{_mandir}/man6/pxboard.6*
%{_mandir}/man6/xboard.6*
%{_mandir}/man6/zic2xpm.6*
%{_infodir}/xboard.info*
%{_desktopdir}/*
%{_pixmapsdir}/*
