%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Stream
Summary:	HTML::Stream perl module
Summary(pl):	Modu³ perla HTML::Stream
Name:		perl-HTML-Stream
Version:	1.54
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Stream perl module.

%description -l pl
Modu³ perla HTML::Stream.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.html docs/index.menu docs/HTML docs/icons etc examples
%{perl_sitelib}/HTML/Stream.pm
%{_mandir}/man3/*
