%global packname  LearnBayes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.12
Release:          1%{?dist}
Summary:          Functions for Learning Bayesian Inference

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
LearnBayes contains a collection of functions helpful in learning the
basic tenets of Bayesian statistical inference. It contains functions for
summarizing basic one and two parameter posterior distributions and
predictive distributions. It contains MCMC algorithms for summarizing
posterior distributions defined by the user.  It also contains functions
for regression models, hierarchical models, Bayesian tests, and
illustrations of Gibbs sampling.

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
%doc %{rlibdir}/LearnBayes/html
%doc %{rlibdir}/LearnBayes/DESCRIPTION
%{rlibdir}/LearnBayes/demo
%{rlibdir}/LearnBayes/INDEX
%{rlibdir}/LearnBayes/help
%{rlibdir}/LearnBayes/data
%{rlibdir}/LearnBayes/NAMESPACE
%{rlibdir}/LearnBayes/R
%{rlibdir}/LearnBayes/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.12-1
- initial package for Fedora