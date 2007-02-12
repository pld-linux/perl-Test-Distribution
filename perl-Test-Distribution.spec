#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Distribution
Summary:	Test::Distribution - perform tests on all modules of a distribution
Summary(pl.UTF-8):   Test::Distribution - wykonywanie testów na wszystkich modułach z dystrybucji
Name:		perl-Test-Distribution
Version:	1.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64dc13f51f60f6022bb8e628f1297957
URL:		http://search.cpan.org/dist/Test-Distribution/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Pod-Coverage >= 0.17
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When using this module in a test script, it goes through all the
modules in your distribution, checks their POD, checks that they
compile ok and checks that they all define a $VERSION.

This module also performs a numer of test on the distribution itself.
It checks that your files match your SIGNATURE file if you have one.
It checks that your distribution isn't missing certain 'core'
description files. It checks to see you haven't missed out listing any
pre-requisites in Makefile.PL.

%description -l pl.UTF-8
W przypadku użycia tego modułu w skrypcie testowym, przechodzi on po
wszystkich modułach w dystrybucji, sprawdzając ich POD, czy się
poprawnie kompilują oraz czy wszystkie definiują $VERSION.

Ten moduł wykonuje także testy na samej dystrybucji. Sprawdza, czy
pliki zgadzają się z plikiem SIGNATURE, jeśli takowy istnieje.
Sprawdza, czy w dystrybucji nie brakuje jakichś głównych plików z
opisem. Sprawdza, czy nie zapomniano wymienić wszystkich zależności w
Makefile.PL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor 

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Distribution.pm
%{_mandir}/man3/*
