%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	HTML-Stream perl module
Summary(pl):	Modu³ perla HTML-Stream
Name:		perl-HTML-Stream
Version:	1.45
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Stream-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTML-Stream perl module

%description -l pl
Modu³ perla HTML-Stream

%prep
%setup -q -n HTML-Stream-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Stream
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README docs/html2perlstream.html docs/HTML/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz docs/*.gz docs/HTML/*.{gz,jpg,gif} etc examples

%{perl_sitelib}/HTML/Stream.pm
%{perl_sitearch}/auto/HTML/Stream

%{_mandir}/man3/*
