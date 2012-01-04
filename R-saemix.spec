%global packname  saemix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.96
Release:          1%{?dist}
Summary:          Stochastic Approximation Expectation Maximization (SAEM) algorithm

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The SAEM package implements the Stochastic Approximation EM algorithm for
parameter estimation in (non)linear mixed effects models. The SAEM
algorithm: - computes the maximum likelihood estimator of the population
parameters, without any approximation of the model (linearization,
quadrature approximation,...), using the Stochastic Approximation
Expectation Maximization (SAEM) algorithm, - provides standard errors for
the maximum likelihood estimator - estimates the conditional modes, the
conditional means and the conditional standard deviations of the
individual parameters, using the Hastings-Metropolis algorithm. Several
applications of SAEM in agronomy, animal breeding and PKPD analysis have
been published by members of the Monolix group

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
%doc %{rlibdir}/saemix/DESCRIPTION
%doc %{rlibdir}/saemix/html
%doc %{rlibdir}/saemix/doc
%{rlibdir}/saemix/data
%{rlibdir}/saemix/R
%{rlibdir}/saemix/INDEX
%{rlibdir}/saemix/help
%{rlibdir}/saemix/NAMESPACE
%{rlibdir}/saemix/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.96-1
- initial package for Fedora