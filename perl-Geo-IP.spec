#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Geo-IP
Version  : 1.51
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Geo-IP-1.51.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Geo-IP-1.51.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgeo-ip-perl/libgeo-ip-perl_1.51-1.debian.tar.xz
Summary  : 'Look up location and network information by IP Address'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Geo-IP-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
Geo::IP - Look up location and network information by IP Address
# VERSION

%package dev
Summary: dev components for the perl-Geo-IP package.
Group: Development
Provides: perl-Geo-IP-devel = %{version}-%{release}

%description dev
dev components for the perl-Geo-IP package.


%package license
Summary: license components for the perl-Geo-IP package.
Group: Default

%description license
license components for the perl-Geo-IP package.


%prep
%setup -q -n Geo-IP-1.51
cd ..
%setup -q -T -D -n Geo-IP-1.51 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Geo-IP-1.51/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Geo-IP
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Geo-IP/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Geo-IP/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Geo/IP.pm
/usr/lib/perl5/vendor_perl/5.28.2/Geo/IP/Record.pm
/usr/lib/perl5/vendor_perl/5.28.2/Geo/IP/Record.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Geo::IP.3
/usr/share/man/man3/Geo::IP::Record.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Geo-IP/LICENSE
/usr/share/package-licenses/perl-Geo-IP/deblicense_copyright
