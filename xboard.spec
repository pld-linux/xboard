Summary:	An X Window System graphical chessboard
Summary(de.UTF-8):	X11-Schnittstelle für GNU-Schach
Summary(es.UTF-8):	Interface X11 para el ajedrez de la GNU
Summary(fr.UTF-8):	Interface X11 au jeu d'échecs de GNU
Summary(pl.UTF-8):	Graficzna szachownica dla X Window
Summary(pt_BR.UTF-8):	Interface X11 para o xadrez da GNU
Summary(ru.UTF-8):	Графический (X11) интерфейс к шахматным программам
Summary(tr.UTF-8):	GNU Chess (satranç) oyununa X11 grafik arabirimi
Summary(uk.UTF-8):	Графічний (X11) інтерфейс до шахових програм
Name:		xboard
Version:	4.9.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnu.org/gnu/xboard/%{name}-%{version}.tar.gz
# Source0-md5:	93d7475bbd69a06ff9cce7add5636beb
Patch0:		%{name}-info.patch
URL:		http://www.tim-mann.org/xboard.html
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	librsvg-devel >= 2.14.0
# pangocairo
BuildRequires:	pango-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Suggests:	crafty
# TODO: package (now it's default program)
#Suggests:	fairymax
Suggests:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xboard is an X Window System based graphical chessboard which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

%description -l de.UTF-8
xboard stellt eine einfach zu bedienende, grafische Oberfläche für
GNU-Schach bereit, so daß Sie sich in stundenlange Schachkämpfe
verwickeln können, ohne komplizierte Befehle lernen zu müssen.Es läßt
sich auch als Frontend zum Austragen von Schachpartien gegen andere
Internet-Benutzer einsetzen.

%description -l es.UTF-8
xboard te ofrece una interface gráfica fácil de usar para el programa
de ajedrez de GNU, permitiendo que aproveches horas de la ación
intelectual sin tener que aprender comandos complicados.

%description -l fr.UTF-8
xboard vous offre une interface graphique facile à utiliser pour le
jeu d'échecs de GNU. Il vous permet d'apprécier les heures de
réflexion des échecs sans avoir à apprendre des commandes complexes.
Il peut aussi être utilisé comme frontal pour jouer aux échecs avec
d'autres personnes sur l'Internet.

%description -l pl.UTF-8
Xboard to graficzna szachownica pod X Window System, używana z
programami szachowymi GNUchess i Crafty, serwerami Internet Chess
(ICS), z szachami przez pocztę elektroniczną itd.

%description -l pt_BR.UTF-8
xboard oferece a você uma interface gráfica fácil de usar para o
programa de xadrez da GNU, permitindo você aproveitar horas da ação
intelectual sem ter que aprender comandos complicados.

%description -l ru.UTF-8
Xboard - это графический интерфейс к шахматным программам, который
может быть использован с программами GNUchess и Crafty, с шахматными
серверами в Интернете (ICS), с шахматами по электронной почте или с
сохраненными записями игр.

%description -l tr.UTF-8
xboard, GNU chess programına grafik arabirimi ekleyerek kullanımı
kolay ve rahat bir ortam sunar. Saatler boyunca kafa yorabilirsiniz.
Internet üzerinden arkadaşınızla da oynayabilirsiniz.

%description -l uk.UTF-8
Xboard - це графічний інтерфейс до шахових програм, який може бути
використаний з програмами GNUchess та Crafty, з шаховими серверами в
Інтернеті (ICS), з шахами по електронній пошті чи із збереженими
записами ігор.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules
%{__make}

%{__make} info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p cmail $RPM_BUILD_ROOT%{_bindir}

echo '.so xboard.6' > $RPM_BUILD_ROOT%{_mandir}/man6/cmail.6
echo '.so xboard.6' > $RPM_BUILD_ROOT%{_mandir}/man6/pxboard.6

# engines integration files (see {gtk,xaw}/xboard.c)
install -d $RPM_BUILD_ROOT%{_datadir}/games/plugins/{logos,xboard}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cmail
%attr(755,root,root) %{_bindir}/xboard
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xboard.conf
%{_datadir}/games/xboard
%dir %{_datadir}/games/plugins
%dir %{_datadir}/games/plugins/logos
%dir %{_datadir}/games/plugins/xboard
%{_datadir}/mime/packages/xboard.xml
%{_desktopdir}/xboard.desktop
%{_desktopdir}/xboard-config.desktop
%{_desktopdir}/xboard-fen-viewer.desktop
%{_desktopdir}/xboard-pgn-viewer.desktop
%{_desktopdir}/xboard-tourney.desktop
%{_iconsdir}/hicolor/48x48/apps/xboard.png
%{_iconsdir}/hicolor/scalable/apps/xboard.svg
%{_mandir}/man6/cmail.6*
%{_mandir}/man6/pxboard.6*
%{_mandir}/man6/xboard.6*
%{_infodir}/xboard.info*
