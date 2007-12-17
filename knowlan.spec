Summary:	Knowlan is ARP protocol based Local Area Network IP and MAC Adress Extractor
Name:		knowlan
Version:	1.0
Release:	%mkrel 1
License:	GPL
Group: 		Monitoring
URL: 		http://www.enderunix.org/knowlan/
Source0:	http://www.enderunix.org/knowlan/%{name}-%{version}-RELEASE.tar.bz2
BuildRequires:	net2-devel
BuildRequires:	libpcap-devel >= 0.7.2

%description
Knowlan is ARP protocol based Local Area Network IP and MAC Adress Extractor.
Knowlan uses libpcap and libnet libraries for to be simple to handle and to
have a simple code for any interestor to deal with the code. To describe
knowlan overally, Knowlan, sends ARP REQUEST packets to the LAN, and at the
same time, It recieves ARP REPLY packets from the up machines. So, It prints
out IP and MAC addresses of online machines.

%prep

%setup -q -n %{name}-%{version}-RELEASE

chmod 644 COPYING ChangeLog INSTALL README TODO

%build

perl -pi -e "s|-Wall|%{optflags} -Wall|g" configure
perl -pi -e "s|\.a|\.so|g" configure
perl -pi -e "s|/lib\b|/%{_lib}|g" configure
	    
./configure

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -m0755 %{name} %{buildroot}%{_sbindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog INSTALL README TODO
%attr(0755,root,root) %{_sbindir}/%{name}
