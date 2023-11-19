# Symbianflo https://abf.io/platforms/rosalinuxro_personal/repositories/main
# spec file under GPLv3


%define mpv_version 0.36
%define gba_version 3184
%define version %{mpv_version}.%{gba_version}
%define oname xt7-player-mpv


Summary:	Xt7-player mpv GUI
Name:		%{oname}
Version:	%{version}
Release:	2
Url:		http://xt7-player.sourceforge.net/xt7forum/
#Source0:	https://github.com/kokoko3k/xt7-player-mpv/archive/%{oname}-%{version}.tar.gz
# using my git this time 
Source0:	https://github.com/abfonly/xt7-player-mpv/archive/refs/tags/%{oname}-v.%{version}.tar.gz
Source100:	%{oname}.rpmlintrc
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
Requires:	ffmpeg >= 4.0.2

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
Requires:	mpv >= 0.36.0

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
%{_iconsdir}/hicolor/*/apps/%{oname}.png
%{_datadir}/applications/%{oname}.desktop
%{_appdatadir}/*.appdata.xml

#-----------------------------------------------------------
%prep
%setup -qn %{oname}-v.%{version}
#%%setup -qn %%{oname}-master

%build
gbc3 -e -a -g -t  -f public-module -f public-control || gbc3 -e -a -g -t -p -m
gba3 || return 1

%install
# executable
mkdir -p %{buildroot}%{_bindir}
install -m755 %{oname}-*.gambas %{buildroot}%{_bindir}/%{oname}.gambas

#icons
for size in 256 48 32 16; do
  install -d %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps
  convert %{oname}.png -resize ${size} %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
done



#menu entry
desktop-file-install  %{oname}.desktop\
	--dir %{buildroot}%{_datadir}/applications
	
#appdata
mkdir -p %{buildroot}%{_appdatadir}
cp -R %{oname}.appdata.xml %{buildroot}%{_appdatadir}/%{oname}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_appdatadir}/*.xml	
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

