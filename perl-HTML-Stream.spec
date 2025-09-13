%define		pdir	HTML
%define		pnam	Stream
Summary:	HTML::Stream - HTML output stream class, and some markup utilities
Summary(pl.UTF-8):	HTML::Stream - klasa produkująca strumień HTML oraz narzędzia do znaczników
Name:		perl-HTML-Stream
Version:	1.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dfc0376eb1359568769e1c22891c24ea
URL:		https://metacpan.org/dist/HTML-Stream
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-HTML-Parser
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::Stream module provides you with an object-oriented (and
subclassable) way of outputting HTML. Basically, you open up an "HTML
stream" on an existing filehandle, and then do all of your output to
the HTML stream. You can intermix HTML-stream-output and
ordinary-print-output, if you like.

%description -l pl.UTF-8
Moduł HTML::Stream udostępnia obiektowo zorientowane (i poddające się
dziedziczeniu) metody do produkowania HTML. Wystarczy otworzyć
"strumień HTML" na istniejącym uchwycie pliku, a następnie przekazywać
całe wyjście do tego strumienia. Można przeplatać wyjście do
strumienia HTML z normalnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*.html docs/index.menu docs/HTML docs/icons etc examples
%{perl_vendorlib}/HTML/Stream.pm
%{_mandir}/man3/HTML::Stream.3pm*
