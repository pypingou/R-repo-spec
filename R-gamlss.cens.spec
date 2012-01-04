%global packname  gamlss.cens
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.4
Release:          1%{?dist}
Summary:          Fitting an interval response variable using gamlss.family distributions

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gamlss R-gamlss.dist R-survival 

BuildRequires:    R-devel tex(latex) R-gamlss R-gamlss.dist R-survival 

%description
This is an add on package to GAMLSS. The purpose of this package is to
allow users to fit interval response variables in GAMLSS models. The main
function gen.cens() generates a censored version of an existing GAMLSS
family distribution.

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
%doc %{rlibdir}/gamlss.cens/html
%doc %{rlibdir}/gamlss.cens/DESCRIPTION
%{rlibdir}/gamlss.cens/help
%{rlibdir}/gamlss.cens/NAMESPACE
%{rlibdir}/gamlss.cens/Meta
%{rlibdir}/gamlss.cens/R
%{rlibdir}/gamlss.cens/data
%{rlibdir}/gamlss.cens/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.4-1
- initial package for Fedora