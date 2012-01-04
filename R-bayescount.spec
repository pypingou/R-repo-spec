%global packname  bayescount
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.9.1
Release:          1%{?dist}
Summary:          Power calculations and Bayesian analysis of count distributions and FECRT data using MCMC

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9.9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-runjags R-coda R-lattice R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-runjags R-coda R-lattice R-stats R-utils 

%description
A set of functions to allow analysis of count data (such as faecal egg
count data) using Bayesian MCMC methods.  Returns information on the
possible values for mean count, coefficient of variation and zero
inflation (true prevalence) present in the data.  A complete faecal egg
count reduction test (FECRT) model is implemented, which returns inference
on the true efficacy of the drug from the pre and post treatment data
provided, using non-parametric bootstrapping as well as using Bayesian
MCMC.  Functions to perform power analyses for faecal egg counts
(including FECRT) are also provided.  Requires Just Another Gibbs Sampler
(JAGS) for most functions (except power analysis calculations), see:

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.9.1-1
- initial package for Fedora