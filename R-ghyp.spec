%global packname  ghyp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.5
Release:          1%{?dist}
Summary:          A package on the generalized hyperbolic distribution and its special cases

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-numDeriv R-graphics R-stats R-gplots 


BuildRequires:    R-devel tex(latex) R-methods R-numDeriv R-graphics R-stats R-gplots



%description
This package provides detailed functionality for working with the
univariate and multivariate Generalized Hyperbolic distribution and its
special cases (Hyperbolic (hyp), Normal Inverse Gaussian (NIG), Variance
Gamma (VG), skewed Student-t and Gaussian distribution). Especially, it
contains fitting procedures, an AIC-based model selection routine, and
functions for the computation of density, quantile, probability, random
variates, expected shortfall and some portfolio optimization and plotting
routines as well as the likelihood ratio test. In addition, it contains
the Generalized Inverse Gaussian distribution.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.5-1
- initial package for Fedora