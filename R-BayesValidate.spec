%global packname  BayesValidate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0
Release:          1%{?dist}
Summary:          BayesValidate Package

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
BayesValidate implements the software validation method described in the
paper "Validation of Software for Bayesian Models using Posterior
Quantiles" (Cook, Gelman, and Rubin, 2005).  It inputs a function to
perform Bayesian inference as well as functions to generate data from the
Bayesian model being fit, and repeatedly generates and analyzes data to
check that the Bayesian inference program works properly.

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
%doc %{rlibdir}/BayesValidate/html
%doc %{rlibdir}/BayesValidate/DESCRIPTION
%{rlibdir}/BayesValidate/NAMESPACE
%{rlibdir}/BayesValidate/R
%{rlibdir}/BayesValidate/help
%{rlibdir}/BayesValidate/INDEX
%{rlibdir}/BayesValidate/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0-1
- initial package for Fedora