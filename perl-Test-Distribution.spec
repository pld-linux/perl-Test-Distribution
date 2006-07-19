#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Distribution
Summary:	perl(Test::Distribution)
Name:		perl-Test-Distribution
Version:	1.26
Release:	0.1
# same as perl
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64dc13f51f60f6022bb8e628f1297957
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-File-Find-Rule
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Distribution - perform tests on all modules of a distribution

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
