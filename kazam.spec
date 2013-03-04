Summary:	A screencasting program created with design in mind
Name:		kazam
Version:	1.0.6
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Multimedia
URL:		https://launchpad.net/kazam
Source0:	%{name}_%{version}.tar.gz
# for automatic typelib() Requires
BuildRequires:	gobject-introspection
BuildRequires:	hicolor-icon-theme
BuildRequires:	intltool
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-distutils-extra
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python-cairo
Requires:	python-gdata
Requires:	python-gobject
Requires:	python-gstreamer-0_10
Requires:	python-xdg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kazam is a simple screen recording program that will capture the
content of your screen and record a video file that can be played by
any video player that supports VP8/WebM video format.

Optionally you can record sound from any sound input device that is
supported and visible by PulseAudio.

%prep
%setup -q -n ubuntu-%{name}
# Upstream shipped two po versions with the same text remove the
# non-standard dir one. to avoid the mess in system locale directory.
rm -rf po/kazam-*.po

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

#%find_lang %{name} --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
#%{_desktopdir}/%{name}.desktop
#%{_iconsdir}/hicolor/*/apps/%{name}.png
#%{_iconsdir}/hicolor/*/apps/youtube.png
#%{_iconsdir}/hicolor/*/status/kazam-*.png
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}-py%{py_ver}.egg-info