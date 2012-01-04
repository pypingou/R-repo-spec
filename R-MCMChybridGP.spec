%global packname  MCMChybridGP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.3
Release:          1%{?dist}
Summary:          Hybrid Markov chain Monte Carlo using Gaussian Processes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Hybrid Markov chain Monte Carlo (MCMC) to simulate from a multimodal
target distribution.  A Gaussian process approximation makes this possible
when derivatives are unknown. The Package serves to minimize the number of
function evaluations in Bayesian calibration of computer models using
parallel tempering.  It allows replacement of the true target distribution
in high temperature chains, or complete replacement of the target. 
Methods used are described in, "Efficient MCMC schemes for Bayesian
calibration of computer models", Fielding, Mark, Nott, David J. and Liong
Shie-Yui, Technometrics (2010). The authors gratefully acknowledge the
support & contributions of the Singapore-Delft Water Alliance (SDWA).  The
research presented in this work was carried out as part of the SDWA's
Multi-Objective Multi-Reservoir Management research programme

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
%doc %{rlibdir}/MCMChybridGP/DESCRIPTION
%doc %{rlibdir}/MCMChybridGP/html
%{rlibdir}/MCMChybridGP/Meta
%{rlibdir}/MCMChybridGP/demo
%{rlibdir}/MCMChybridGP/libs
%{rlibdir}/MCMChybridGP/NAMESPACE
%{rlibdir}/MCMChybridGP/R
%{rlibdir}/MCMChybridGP/help
%{rlibdir}/MCMChybridGP/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.3-1
- initial package for Fedora