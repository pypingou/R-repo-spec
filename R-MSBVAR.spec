%global packname  MSBVAR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Markov-Switching, Bayesian, Vector Autoregression Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-KernSmooth R-xtable R-coda R-bit R-mvtnorm R-lattice 

BuildRequires:    R-devel tex(latex) R-KernSmooth R-xtable R-coda R-bit R-mvtnorm R-lattice 

%description
Provides methods for estimating frequentist and Bayesian Vector
Autoregression (VAR) models and Markov-switching Bayesian VAR (MSBVAR). 
Functions for reduced form and structural VAR models are also available.
Includes methods for the generating posterior inferences for these models,
forecasts, impulse responses (using likelihood-based error bands), and
forecast error decompositions.  Also includes utility functions for
plotting forecasts and impulse responses, and generating draws from
Wishart and singular multivariate normal densities.  Current version
includes functionality to build and evaluate models with Markov switching.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.0-1
- initial package for Fedora