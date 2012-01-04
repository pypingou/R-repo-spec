%global packname  tgp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.2
Release:          1%{?dist}
Summary:          Bayesian treed Gaussian process models

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.4-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Bayesian nonstationary, semiparametric nonlinear regression and design by
treed Gaussian processes (GPs) with jumps to the limiting linear model
(LLM).  Special cases also implemented include Bayesian linear models,
CART, treed linear models, stationary separable and isotropic GPs, and GP
single-index models.  Provides 1-d and 2-d plotting functions (with
projection and slice capabilities) and tree drawing, designed for
visualization of tgp-class output.  Sensitivity analysis and
multi-resolution models are supported. Sequential experimental design and
adaptive sampling functions are also provided, including ALM, ALC, and
expected improvement.  The latter supports derivative-free optimization of
noisy black-box functions.

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
%doc %{rlibdir}/tgp/html
%doc %{rlibdir}/tgp/DESCRIPTION
%doc %{rlibdir}/tgp/doc
%doc %{rlibdir}/tgp/CITATION
%{rlibdir}/tgp/NAMESPACE
%{rlibdir}/tgp/INDEX
%{rlibdir}/tgp/LICENSE
%{rlibdir}/tgp/R
%{rlibdir}/tgp/help
%{rlibdir}/tgp/libs
%{rlibdir}/tgp/data
%{rlibdir}/tgp/Meta
%{rlibdir}/tgp/._doc
%{rlibdir}/tgp/demo
%{rlibdir}/tgp/._CITATION

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.2-1
- initial package for Fedora