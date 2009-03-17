
%define realname   Test-Most
%define version    0.20
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Internal exception class
Source:     http://www.cpan.org/modules/by-module/Test/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
no description found

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


