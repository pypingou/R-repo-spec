%global packname  list
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.2
Release:          1%{?dist}
Summary:          Statistical Methods for the Item Count Technique and List Experiment

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-VGAM R-magic R-gamlss.dist R-MASS R-quadprog R-arm R-corpcor R-mvtnorm R-sandwich R-coda 


BuildRequires:    R-devel tex(latex) R-utils R-VGAM R-magic R-gamlss.dist R-MASS R-quadprog R-arm R-corpcor R-mvtnorm R-sandwich R-coda



%description
list is a publicly available R package that allows researchers to conduct
multivariate statistical analyses of survey data with list experiments. In
addition, the package implements the statistical test that is designed to
detect certain failures of list experiments. This survey methodology is
also known as the item count technique or the unmatched count technique
and is an alternative to the commonly used randomized response method. The
package implements the methods developed by Imai (2010) and Blair and Imai
(2010), and a Bayesian MCMC implementation of regression for the standard
and multiple sensitive item list experiment designs.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.2-1
- initial package for Fedora