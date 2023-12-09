# Symbianflo https://abf.io/platforms/rosalinuxro_personal/repositories/main
# spec file under GPLv3

%define distsuffix mrb
%define mpv_version 0.37
%define gba_version 3184
%define version %{mpv_version}.%{gba_version}



Summary:	Xt7-player mpv GUI
Name:		xt7-player-mpv
Version:	%{version}
Release:	1
Url:		http://xt7-player.sourceforge.net/xt7forum/
Source0:	https://github.com/abfonly/xt7-player-mpv/archive/refs/tags/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
License:	GPLv3
Group:		Video

BuildArch:	noarch

BuildRequires:	gambas3-devel >= 3.18.4
BuildRequires:	gambas3-runtime >= 3.18.4
BuildRequires:	gambas3-gb-qt5 >= 3.18.4
BuildRequires:	gambas3-gb-qt5-ext >= 3.18.4
BuildRequires:	gambas3-gb-qt5-x11 >= 3.18.4
BuildRequires:	gambas3-gb-form >= 3.18.4
BuildRequires:	gambas3-gb-desktop >= 3.18.4
BuildRequires:	gambas3-gb-form-mdi >= 3.18.4
BuildRequires:	gambas3-gb-net >= 3.18.4
BuildRequires:	gambas3-gb-net-curl >= 3.18.4
BuildRequires:	gambas3-gb-settings >= 3.18.4
BuildRequires:	gambas3-gb-xml >= 3.18.4
BuildRequires:	gambas3-gb-web >= 3.18.4
BuildRequires:	gambas3-gb-image >= 3.18.4
BuildRequires:	gambas3-gb-image-imlib >= 3.18.4
BuildRequires:	gambas3-gb-image-io >= 3.18.4
BuildRequires:	gambas3-gb-db >= 3.18.4
BuildRequires:	gambas3-gb-dbus >= 3.18.4
BuildRequires:	gambas3-gb-db-form >= 3.18.4
BuildRequires:	pkgconfig(taglib)
BuildRequires:	gambas3-gb-gui >= 3.18.4
BuildRequires:	gambas3-gb-compress >= 3.18.4
BuildRequires:	gambas3-gb-form-dialog >= 3.18.4
BuildRequires:	gambas3-gb-signal >= 3.18.4
BuildRequires:	gambas3-gb-libxml >= 3.18.4
BuildRequires:	gambas3-gb-form-stock  >= 3.18.4
BuildRequires:	gambas3-gb-util-web >= 3.18.4
BuildRequires:	gambas3-gb-args >= 3.18.4


# 4 desktop file install/check
BuildRequires:	desktop-file-utils

# 4 appdata file
BuildRequires:	appstream-util

# 4 icons convert
BuildRequires:	imagemagick

# 4 dvb-epg
Requires:	dvbsnoop
Requires:	dvb-apps

# 4 downloading from youtube
Requires:	yt-dlp
Requires:	xterm
Requires:	wget
Requires:	gambas3-gb-util-web >= 3.18.4

# 4 audio extract/convert
Requires:	ffmpeg >= 6.0

# 4 subtiles , manage, download a.s.o.
Requires:	python >= 3.8

# 4 global hotkeys support
Requires:	xbindkeys

# 4 desktop integration
Requires:	xdg-utils

# 4 tagging
Requires:	%{_lib}taglib1
Requires:	%{_lib}taglib_c0

# default player
Requires:	mpv >= 0.37.0

# 4 GUI
Requires:	gambas3-runtime >= 3.18.4
Requires:	gambas3-gb-image >= 3.18.4
Requires:	gambas3-gb-dbus >= 3.18.4
Requires:	gambas3-gb-gtk3 >= 3.18.4
Requires:	gambas3-gb-gui >= 3.18.4
Requires:	gambas3-gb-form >= 3.18.4
Requires:	gambas3-gb-xml >= 3.18.4
Requires:	gambas3-gb-qt5 >= 3.18.4
Requires:	gambas3-gb-qt5-ext >= 3.18.4
Requires:	gambas3-gb-qt5-x11 >= 3.18.4
Requires:	gambas3-gb-form-stock  >= 3.18.4
Requires:	gambas3-gb-net >= 3.18.4
Requires:	gambas3-gb-form-dialog >= 3.18.4
Requires:	gambas3-gb-settings >= 3.18.4
Requires:	gambas3-gb-form-mdi >= 3.18.4
Requires:	gambas3-gb-compress >= 3.18.4
Requires:	gambas3-gb-desktop >= 3.18.4
Requires:	gambas3-gb-web >= 3.18.4
Requires:	gambas3-gb-net-curl >= 3.18.4
Requires:	gambas3-gb-signal >= 3.18.4
Requires:	gambas3-gb-args >= 3.18.4
Requires:	fonts-ttf-droid

# 4 icecast / shoutcast
Requires:	gambas3-gb-libxml >= 3.18.4

# mplayer based is obsolete
Provides:	Xt7-player3 = %{EVRD}
Provides:	xt7-player3 = %{EVRD}

Obsoletes: xt7-player3 < %{EVRD}
Obsoletes: Xt7-player3 < %{EVRD}

AutoReqProv:	no

%description
Xt7-Player, an complete mpv GUI
This program is written in Gambas3, so you will need Gambas3 to be installed.

%files
%doc LICENSE.TXT README.* CHANGELOG_GIT
%{_bindir}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_appdatadir}/*.appdata.xml

#-----------------------------------------------------------
%prep
%autosetup

%build
./makefile

%install
./makeinstall
cd build && cp -R -t %{buildroot} *

%check
appstream-util validate-relax --nonet %{buildroot}%{_appdatadir}/*.xml	
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

