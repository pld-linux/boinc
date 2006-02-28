# TODO:
#	- check for BR-s
#	- check configure options
#	- create devel and static subpackages
#	- package boinc script into separate package
#	- package BOINC server in separate package
#	- build files section
#	- maybe BOINC.spec
#	- find out license
#	- fix linking for amd64 arch
#	- wxGTK2-devel or wxGTK2-unicode-devel or wxGTK2-univ-devel or wxGTK2-univ-unicode-devel ??

Summary:	BOINC - Berkeley Open Infrastructure for Network Computing
Summary(pl):	BOINC - otwarta infrastruktura Berkeley do obliczeñ sieciowych
Name:		boinc
Version:	5.3.22
Release:	0.2
License:	GPL
Group:		Applications
# Source generated from:
# cvs -d :pserver:anonymous:@alien.ssl.berkeley.edu:/home/cvs/cvsroot checkout -r boinc_core_release_5_3_22 boinc
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	c2a9af4f22e37b5a44a3ca45aa7eb843
Source1:	http://phileimer.9online.fr/%{name}-1.10.tar.bz2
# Source1-md5:	85907bd0b9b3527ee90ee73ad2d4ea8d
Patch0:		%{name}-include.patch
Patch1:		%{name}-Makefile.am.patch
Patch2:		%{name}-platform.patch
#Patch for boinc script not used for now don't delete
#Patch2:	%{name}-path.patch
URL:		http://boinc.berkeley.edu/
# URL for boinc script
#URL:		http://phileimer.9online.fr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	wxGTK2-devel
BuildRequires:	wxWidgets-devel
ExclusiveArch:	%{ix86} amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BOINC is a software platform for distributed computing using
volunteered computer resources.

%description -l pl
BOINC (Berkeley Open Infrastructure for Network Computing) to
platforma programowa do rozproszonych obliczeñ przy u¿yciu zasobów
komputerowych ochotników.

%package script
Summary:	boinc - a bash script used to manage boinc client
Summary(pl):	boinc - napisany w bashu skrypt do zarz±dzania klientem boinc
Group:		Applications
URL:		http://phileimer.9online.fr/

%description script
boinc is a bash script for unix like systems used to manage client of
the BOINC project (Berkeley Open Infrastructure for Network
Computing).

%description script -l pl
boinc to napisany w bashu skrypt dla systemów uniksowych s³u¿±cy do
zarz±dzania klientem projektu BOINC (Berkeley Open Infrastructure for
Network Computing).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
mv clientgui/BOINCDial{u,U}pManager.h
mv clientgui/BOINCDial{u,U}pManager.cpp

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
%ifarch amd64
	--with-boinc-platform=i686-pc-linux-gnu \
%endif
	--enable-static \
	--enable-shared \
	--with-x \
	--with-ssl \
	--with-wx-config=/usr/bin/wx-gtk2-ansi-config

%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%%install
#rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_bindir}

#install boinc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/
%attr(755,root,root) %{_bindir}/*
