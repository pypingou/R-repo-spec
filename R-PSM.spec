%global packname  PSM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.5
Release:          1%{?dist}
Summary:          Non-Linear Mixed-Effects modelling using Stochastic Differential Equations.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-numDeriv R-odesolve R-ucminf 

BuildRequires:    R-devel tex(latex) R-MASS R-numDeriv R-odesolve R-ucminf 

%description
This package provides functions for estimation of linear and non-linear
mixed-effects models using stochastic differential equations. Moreover it
provides functions for finding smoothed estimates of model states and for
simulation. The package allows for any multivariate non-linear
time-variant model to be specified, and it also handels multidimentional
input, co-variates, missing observations and specification of dosage

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
%doc %{rlibdir}/PSM/html
%doc %{rlibdir}/PSM/DESCRIPTION
%doc %{rlibdir}/PSM/doc
%{rlibdir}/PSM/INDEX
%{rlibdir}/PSM/R
%{rlibdir}/PSM/NAMESPACE
%{rlibdir}/PSM/libs
%{rlibdir}/PSM/help
%{rlibdir}/PSM/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.5-1
- initial package for Fedora