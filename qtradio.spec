%define name	qtradio
%define version	0.8.1
%define release	%mkrel 9

Summary:	QtRadio - listen to the radio with QtRadio
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		https://linux.perlak.com/project.php?prj_name=qtradio
Group:		Sound
Source0:	%{name}-%{version}.tar.bz2
#Source1:	%{name}_16.png
#Source2:	%{name}_32.png
#Source3:	%{name}_48.png
# Patch0: use skins in /usr/share, not /usr/local/share
Patch0:		%{name}-0.8.0-path.patch.bz2
Patch1:		%{name}-0.8.1-compile.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	qt3-devel

%description
QtRadio - listen to the radio with QtRadio.
It should work with every FM tuner card that is supported
by video4linux. 
It has support for remote controls via lirc-support
and recording to file.


%prep
%setup -q -n QtRadio-%{version}
%patch0 -p1 -b .path
%patch1 -p1 -b .compile

%build
export QTDIR=%{_prefix}/lib/qt3 ; export QTLIB=$QTDIR/%{_lib}
%configure

%make

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

# Not installed with make install
mkdir -p %{buildroot}/%{_datadir}/QtRadio
cp -f -R QtRadio %{buildroot}/%{_datadir}


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications//menu
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%name
Name=QtRadio
Comment=QtRadio - listen to the radio with QtRadio.
Categories=Audio;
EOF

install -d %buildroot/%_miconsdir
install -d %buildroot/%_liconsdir
install -d %buildroot/%_iconsdir

# Todo: icons
#install -m644 %SOURCE1 %buildroot/%_miconsdir/%name.png
#install -m644 %SOURCE2 %buildroot/%_iconsdir/%name.png
#install -m644 %SOURCE3 %buildroot/%_liconsdir/%name.png

%{find_lang} %name


%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%dir %{_datadir}/QtRadio
%{_datadir}/QtRadio/*
#%{_datadir}/icons/*
%{_datadir}/applications/mandriva-%{name}.desktop


