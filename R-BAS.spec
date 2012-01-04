%global packname  BAS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.92
Release:          1%{?dist}
Summary:          Bayesian Model Averaging using Bayesian Adaptive Sampling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Package for Bayesian Model Averaging in linear models using stochastic or
deterministic sampling without replacement from posterior distributions.
Prior distributions on coefficients are from Zellner's g-prior or mixtures
of g-priors corresponding to the Zellner-Siow Cauchy Priors or the Liang
et al hyper-g priors (JASA 2008). Other model selection criterian include
AIC and BIC. Sampling probabilities may be updated based on the sampled
models. Allows uniform or beta-binomial prior distributions on models.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.92-1
- initial package for Fedora