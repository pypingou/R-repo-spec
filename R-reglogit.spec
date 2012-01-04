%global packname  reglogit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Simulation-based Regularized Logistic Regression

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-mvtnorm R-boot 

BuildRequires:    R-devel tex(latex) R-methods R-mvtnorm R-boot 

%description
Regularized logistic regression by Gibbs sampling. The package implements
subtly different MCMC schemes with varying efficiency depending on the
data type (binary v. binomial, say) and the desired estimator (regularized
maximum likelihood, or Bayesian maximum a posteriori/posterior mean, etc.)
through a unified interface

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
%doc %{rlibdir}/reglogit/DESCRIPTION
%doc %{rlibdir}/reglogit/html
%{rlibdir}/reglogit/R
%{rlibdir}/reglogit/INDEX
%{rlibdir}/reglogit/LICENSE
%{rlibdir}/reglogit/NAMESPACE
%{rlibdir}/reglogit/help
%{rlibdir}/reglogit/Meta
%{rlibdir}/reglogit/data
%{rlibdir}/reglogit/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora