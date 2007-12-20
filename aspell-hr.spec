%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.51-0
%define languageenglazy Croatian
%define languagecode hr
%define lc_ctype hr_HR

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.51.0
Release:       %mkrel 3
Group:         System/Internationalization
Source:	       http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   LGPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/aspell
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/aspell

chmod 644 Copyright README* doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*

