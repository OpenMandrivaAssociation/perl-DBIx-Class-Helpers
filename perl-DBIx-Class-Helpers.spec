%define upstream_name    DBIx-Class-Helpers
%define upstream_version 2.007000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Simplify the common case stuff for DBIx::Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Candy)
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(String::CamelCase)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildArch:	noarch

%description
A collection of various helper utilities for the DBIx::Class manpage stuff.
Probably only useful for components.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.7.0-2mdv2011.0
+ Revision: 657403
- rebuild for updated spec-helper

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.0-1
+ Revision: 646331
- update to new version 2.007000

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-1
+ Revision: 635784
- update to new version 2.006000

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 2.5.0-1mdv2011.0
+ Revision: 624962
- import perl-DBIx-Class-Helpers

