Summary:	An X Window System graphical chessboard
Summary(de):	X11-Schnittstelle f�r GNU-Schach
Summary(es):	Interface X11 para el ajedrez de la GNU
Summary(fr):	Interface X11 au jeu d'�checs de GNU
Summary(pl):	Graficzna szachownica dla X Window
Summary(pt_BR):	Interface X11 para o xadrez da GNU
Summary(ru):	����������� (X11) ��������� � ��������� ����������
Summary(tr):	GNU Chess (satran�) oyununa X11 grafik arabirimi
Summary(uk):	���Ʀ���� (X11) ��������� �� ������� �������
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
xboard stellt eine einfach zu bedienende, grafische Oberfl�che f�r
GNU-Schach bereit, so da� Sie sich in stundenlange Schachk�mpfe
verwickeln k�nnen, ohne komplizierte Befehle lernen zu m�ssen.Es l��t
sich auch als Frontend zum Austragen von Schachpartien gegen andere
Internet-Benutzer einsetzen.

%description -l es
xboard te ofrece una interface gr�fica f�cil de usar para el programa
de ajedrez de GNU, permitiendo que aproveches horas de la aci�n
intelectual sin tener que aprender comandos complicados.

%description -l fr
xboard vous offre une interface graphique facile � utiliser pour le
jeu d'�checs de GNU. Il vous permet d'appr�cier les heures de
r�flexion des �checs sans avoir � apprendre des commandes complexes.
Il peut aussi �tre utilis� comme frontal pour jouer aux �checs avec
d'autres personnes sur l'Internet.

%description -l pl
Xboard to graficzna szachownica pod X Window System, u�ywana z
programami szachowymi GNUchess i Crafty, serwerami Internet Chess
(ICS), z szachami przez poczt� elektroniczn� itd.

%description -l pt_BR
xboard oferece a voc� uma interface gr�fica f�cil de usar para o
programa de xadrez da GNU, permitindo voc� aproveitar horas da a��o
intelectual sem ter que aprender comandos complicados.

%description -l ru
Xboard - ��� ����������� ��������� � ��������� ����������, �������
����� ���� ����������� � ����������� GNUchess � Crafty, � ����������
��������� � ��������� (ICS), � ��������� �� ����������� ����� ��� �
������������ �������� ���.

%description -l tr
xboard, GNU chess program�na grafik arabirimi ekleyerek kullan�m�
kolay ve rahat bir ortam sunar. Saatler boyunca kafa yorabilirsiniz.
Internet �zerinden arkada��n�zla da oynayabilirsiniz.

%description -l uk
Xboard - �� ���Ʀ���� ��������� �� ������� �������, ���� ���� ����
������������ � ���������� GNUchess �� Crafty, � �������� ��������� �
�������Ԧ (ICS), � ������ �� ��������Φ� ���Ԧ �� �� �����������
�������� ����.

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
