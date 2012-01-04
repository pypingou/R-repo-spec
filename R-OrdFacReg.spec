%global packname  OrdFacReg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Least squares, logistic, and Cox-regression with ordered predictors

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-eha R-MASS 

BuildRequires:    R-devel tex(latex) R-eha R-MASS 

%description
In biomedical studies, researchers are often interested in assessing the
association between one or more ordinal explanatory variables and an
outcome variable, at the same time adjusting for covariates of any type.
The outcome variable may be continuous, binary, or represent censored
survival times. In the absence of a precise knowledge of the response
function, using monotonicity constraints on the ordinal variables improves
efficiency in estimating parameters, especially when sample sizes are
small. This package implements an active set algorithm that efficiently
computes such estimators.

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
%doc %{rlibdir}/OrdFacReg/html
%doc %{rlibdir}/OrdFacReg/NEWS
%doc %{rlibdir}/OrdFacReg/DESCRIPTION
%{rlibdir}/OrdFacReg/help
%{rlibdir}/OrdFacReg/R
%{rlibdir}/OrdFacReg/INDEX
%{rlibdir}/OrdFacReg/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora