%global packname  MCMCpack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Markov chain Monte Carlo (MCMC) Package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-coda R-MASS R-stats 

BuildRequires:    R-devel tex(latex) R-coda R-MASS R-stats 

%description
This package contains functions to perform Bayesian inference using
posterior simulation for a number of statistical models. Most simulation
is done in compiled C++ written in the Scythe Statistical Library Version
1.0.2. All models return coda mcmc objects that can then be summarized
using the coda package.  MCMCpack also contains some useful utility
functions, including some additional density functions and pseudo-random
number generators for statistical distributions, a general purpose
Metropolis sampling algorithm, and tools for visualization.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora