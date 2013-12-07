%define modname	Test-Most
%define modver	0.24

Summary:	Most commonly needed test functions and features
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Module::Build::Compat)
Requires:	perl(Exception::Class)
Requires:	perl(Test::Deep)
Requires:	perl(Test::Differences)
Requires:	perl(Test::Exception)
Requires:	perl(Test::Warn)

%description
Most commonly needed test functions and features.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*

