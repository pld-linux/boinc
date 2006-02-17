# TODO:
#	- check for BR-s
#	- check configure options
#	- create devel and static subpackages
#	- package boinc script into separate package
#	- build files section
#	- maybe BOINC.spec
#	- find out license

Summary:	BOINC - Berkeley Open Infrastructure for Network Computing
Summary(pl):	BOINC - otwarta infrastruktura Berkeley do obliczeñ sieciowych
Name:		boinc
Version:	5.3.19
Release:	0.1
License:	GPL
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	96281927b4f4288db389d58fc548c83b
Source1:	http://phileimer.9online.fr/%{name}-1.10.tar.bz2
# Source1-md5:	85907bd0b9b3527ee90ee73ad2d4ea8d
Patch0:		%{name}-include.patch
Patch1:		%{name}-path.patch
URL:		http://phileimer.9online.fr/
BuildRequires:	curl-devel
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRequires:	wxWidgets-devel
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
mv clientgui/BOINCDial{u,U}pManager.h

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
