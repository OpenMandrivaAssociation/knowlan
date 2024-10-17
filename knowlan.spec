Summary:	ARP protocol based Local Area Network IP and MAC Adress Extractor
Name:		knowlan
Version:	1.0
Release:	9
License:	GPL
Group: 		Monitoring
URL: 		https://www.enderunix.org/knowlan/
Source0:	http://www.enderunix.org/knowlan/%{name}-%{version}-RELEASE.tar.bz2
BuildRequires:	net-devel >= 1.1.3
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
install -d %{buildroot}%{_sbindir}
install -m0755 %{name} %{buildroot}%{_sbindir}/

%clean

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog INSTALL README TODO
%attr(0755,root,root) %{_sbindir}/%{name}


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 620013
- the mass rebuild of 2010.0 packages

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2010.0
+ Revision: 382700
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2009.1
+ Revision: 298269
- rebuilt against libpcap-1.0.0

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 247811
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2008.1
+ Revision: 170930
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jun 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.0
+ Revision: 37312
- Import knowlan



* Thu May 25 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package
