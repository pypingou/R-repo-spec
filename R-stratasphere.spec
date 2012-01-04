%global packname  stratasphere
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Stratified Spherical Approximate Conditional Modeling

Group:            Applications/Engineering 
License:          Apache License 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival R-mboost R-hash 

BuildRequires:    R-devel tex(latex) R-survival R-mboost R-hash 

%description
For data where the observations occur or are collected in a stratified
fashion, the strata level effect is sometimes not of interest or is simply
impossible to estimate. Conditioning on the strata eliminates these
difficulties, but leads to a combinatorially complex calculation. The
spherical approximate method replaces this complex calculation with a
closed form solution, leading to a simple fixed point iteration method for
fitting the linear model.  This package implements linear model fitting
via Stratasphere(), and stepwise regression and boosting extensions via
StratasphereStep() and StratasphereBoost(), respectively. Note that this
package is distributed under the Apache 2.0 license.

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
%doc %{rlibdir}/stratasphere/html
%doc %{rlibdir}/stratasphere/DESCRIPTION
%{rlibdir}/stratasphere/LICENSE
%{rlibdir}/stratasphere/Meta
%{rlibdir}/stratasphere/INDEX
%{rlibdir}/stratasphere/R
%{rlibdir}/stratasphere/NAMESPACE
%{rlibdir}/stratasphere/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora