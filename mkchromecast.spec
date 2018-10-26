%global gitdate 20181026
%global commit0 c913e0ee62b82566b414ea61834b638f82eee042
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           mkchromecast
Version:        0.3.9
Release:        2%{?dist}
Summary:        Cast audio and video from your Linux desktop to your Google Cast device
Group:          Applications/Multimedia
License:        MIT
URL:            http://mkchromecast.com/
# devel branch
Source0:	https://github.com/muammar/mkchromecast/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch

#----------------------------------------
Requires: python3-mutagen
Requires: python3-flask
Requires: python3-netifaces
Requires: python3-psutil
Requires: python3-chromecast
Requires: python3-requests
Requires: python3-qt5
Requires: python3-PyYAML
Requires: python3-werkzeug
Requires: sox
Requires: lame
Requires: flac
Requires: youtube-dl
Requires: nodejs
Requires: ffmpeg
Recommends: pulseaudio
Recommends: pavucontrol
Recommends: python3-soco
#--------------------------------------

%description
This is a python program to cast audio and video from your Linux desktop
to your GoogleCast devices or Sonos speakers. It is written in Python, 
and it streams via node.js, ffmpeg, or avconv.


%prep
%autosetup -n %{name}-%{commit0} 

%build

%install
  install -d "%{buildroot}/usr/bin/"
  install -d "%{buildroot}/usr/share/%{name}/"
  install -d "%{buildroot}/usr/share/%{name}/%{name}/getch/"
  install -d "%{buildroot}/usr/share/%{name}/images/"
  install -d "%{buildroot}/usr/share/%{name}/nodejs/"

  install -D -m755 bin/%{name} "%{buildroot}/usr/share/%{name}/%{name}.py"
  ln -s "/usr/share/%{name}/%{name}.py" "%{buildroot}/usr/bin/%{name}"

  install -D -m644 mkchromecast/*.py "%{buildroot}/usr/share/%{name}/%{name}/"
  install -D -m644 mkchromecast/getch/* "%{buildroot}/usr/share/%{name}/%{name}/getch/"
  install -D -m644 images/*.png "%{buildroot}/usr/share/%{name}/images/"
  install -D -m644 nodejs/html5-video-streamer.js "%{buildroot}/usr/share/%{name}/nodejs/"


  install -D -m644 "man/%{name}.1" "%{buildroot}/usr/share/man/man1/%{name}.1"
  install -D -m644 "images/%{name}.xpm" "%{buildroot}/usr/share/pixmaps/%{name}.xpm"
  install -D -m644 "%{name}.desktop" "%{buildroot}/usr/share/applications/%{name}.desktop"

%files
%license LICENSE
%{_bindir}/mkchromecast
%{_datadir}/applications/mkchromecast.desktop
%{_mandir}/man1/mkchromecast.1.gz
%{_datadir}/mkchromecast/
%{_datadir}/pixmaps/mkchromecast.xpm


%changelog

* Fri Oct 26 2018 David Va <davidva AT tuta DOT io> 0.3.9.2-1 
- Updated to current commit

* Thu Aug 02 2018 David Va <davidva AT tuta DOT io> 0.3.9.1-1 
- Initial build
