%define upstream_name    Parse-CPAN-Packages-Fast
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse CPAN's package index
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN::DistnameInfo)
BuildRequires: perl(PerlIO::gzip)
BuildRequires: perl(version)
BuildArch: noarch

%description
This is a largely API compatible rewrite of the Parse::CPAN::Packages
manpage.

Notable differences are

* * The method add_package of
  Parse::CPAN::Packages::Fast::Distribution is not implemented

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


