%global packname  weightedScores
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Weighted scores method for regression with dependent data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-rootSolve 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-rootSolve 

%description
This package has functions that handle the steps for the weighted scores
method in Nikoloulopoulos, Joe and Chaganty (2011, Biostatistics, 12:
653-665) for binary (logistic and probit), Poisson and negative binomial
regression, with dependent data. Two versions of negative binomial
regression from Cameron and Trivedi (1998) are used. Let NB(tau,xi) be a
parametrization with probability mass function f(y;tau,xi)= Gamma(tau+y)
xi^y / [ Gamma(tau) y! (1+xi)^(tau+y)], for y=0,1,2,..., tau>0, xi>0, with
mean mu=tau*xi = exp(beta^T x) and variance tau*xi*(1+xi), where x is a
vector of covariates. For NB1, the parameter gamma is defined so that
tau=mu/gamma, xi=gamma; for NB2, the parameter gamma is defined so that
tau=1/gamma, xi=mu*gamma.  In NB1, the convolution parameter tau is a
function of the covariate x and xi is constant; in NB2, the convolution
parameter tau is constant and xi is a function of the covariate x.

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
%doc %{rlibdir}/weightedScores/DESCRIPTION
%doc %{rlibdir}/weightedScores/html
%{rlibdir}/weightedScores/data
%{rlibdir}/weightedScores/NAMESPACE
%{rlibdir}/weightedScores/R
%{rlibdir}/weightedScores/INDEX
%{rlibdir}/weightedScores/help
%{rlibdir}/weightedScores/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora