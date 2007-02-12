#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	LibXML-Iterator
Summary:	XML::LibXML::Iterator - XML::LibXML's Tree Iteration Class
Summary(pl.UTF-8):   XML::LibXML::Iterator - klasa iteratora dla drzew XML::LibXML
Name:		perl-XML-LibXML-Iterator
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5139c75dc8cde4db19059fb62f44ac5b
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.52
BuildRequires:	perl-XML-NodeFilter
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-LibXML >= 1.52
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::LibXML::Iterator implements the iterator part of the DOM
Traversal and Range specification. This class allows to iterate
through a DOM as it is done through an ordinary array.

%description -l pl.UTF-8
XML::LibXML::Iterator implementuje część dotyczącą iteratora ze
specyfikacji "DOM Traversal and Range". Klasa ta pozwala na
przemieszczanie po DOM tak, jak po zwykłej tablicy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/XML/LibXML
%{perl_vendorlib}/XML/LibXML/Iterator.pm
%{perl_vendorlib}/XML/LibXML/NodeList
%{_mandir}/man3/*
