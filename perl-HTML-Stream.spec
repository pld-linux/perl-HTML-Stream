%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Stream
Summary:	HTML::Stream - HTML output stream class, and some markup utilities
Summary(pl):	HTML::Stream - klasa produkuj�ca strumie� HTML oraz narz�dza do znacznik�w
Name:		perl-HTML-Stream
Version:	1.54
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-HTML-Parser
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::Stream module provides you with an object-oriented (and
subclassable) way of outputting HTML. Basically, you open up an "HTML
stream" on an existing filehandle, and then do all of your output to
the HTML stream. You can intermix HTML-stream-output and
ordinary-print-output, if you like.

%description -l pl
Modu� HTML::Stream udost�pnia obiektowo zorientowane (i poddaj�ce si�
dziedziczeniu) metody do produkowania HTML. Wystarczy otworzy�
"strumie� HTML" na istniej�cym uchwycie pliku, a nast�pnie przekazywa�
ca�e wyj�cie do tego strumienia. Mo�na przeplata� wyj�cie do
strumienia HTML z normalnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*.html docs/index.menu docs/HTML docs/icons etc examples
%{perl_sitelib}/HTML/Stream.pm
%{_mandir}/man3/*
