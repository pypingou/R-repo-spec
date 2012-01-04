%global packname  BMS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Bayesian Model Averaging Library

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Bayesian Model Averaging for linear models with a wide choice of
(customizable) priors. Built-in priorss include coefficient priors (fixed,
flexible and hyper-g priors), 5 kinds of model priors, moreover model
sampling by enumeration or various MCMC approaches. Post-processing
functions allow for inferring posterior inclusion and model
probabilitites, various moments, coefficient and predictive densities.
Plotting functions available for posterior model size, MCMC convergence,
predictive and coefficient densities, best models representation, BMA

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora