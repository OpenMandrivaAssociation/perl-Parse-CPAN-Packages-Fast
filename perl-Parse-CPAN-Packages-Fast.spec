%define upstream_name    Parse-CPAN-Packages-Fast
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Parse CPAN's package index
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires:	perl(CPAN::Version)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(PerlIO::gzip)
BuildArch:	noarch

%description
This is a largely API compatible rewrite of the Parse::CPAN::Packages
manpage.

Notable differences are

* * The method add_package of
  Parse::CPAN::Packages::Fast::Distribution is not implemented

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
%doc Changes META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

