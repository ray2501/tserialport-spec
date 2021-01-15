%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tserialport
Summary:       tcl package for for library libserialport
Version:       1.1
Release:       0
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        tserialport1.1.tar.gz
URL:           https://sourceforge.net/projects/tclsnippets/
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.5
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
libserialport is a minimal, cross-platform shared library written in C
that is intended to take care of the OS-specific details when writing software
that uses serial ports.

tserialport is tcl package for library libserialport.

%prep
%setup -q -n %{name}%{version}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc LICENSE.serialport license.terms
%defattr(-,root,root)
%{tcl_archdir}
/usr/share/man/mann

