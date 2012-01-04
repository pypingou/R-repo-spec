%global packname  RcmdrPlugin.doex
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Rcmdr plugin for Stat 4309 course

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-multcomp 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-multcomp 

%description
This package provides an Rcmdr "plug-in" based on the Design of
experiments class Stat 4309

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/RcmdrPlugin.doex/html
%doc %{rlibdir}/RcmdrPlugin.doex/DESCRIPTION
%{rlibdir}/RcmdrPlugin.doex/R
%{rlibdir}/RcmdrPlugin.doex/NAMESPACE
%{rlibdir}/RcmdrPlugin.doex/INDEX
%{rlibdir}/RcmdrPlugin.doex/etc
%{rlibdir}/RcmdrPlugin.doex/Meta
%{rlibdir}/RcmdrPlugin.doex/help

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora