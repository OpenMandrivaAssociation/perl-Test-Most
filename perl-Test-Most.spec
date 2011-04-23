%define upstream_name    Test-Most
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Most commonly needed test functions and features
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
