%global packname  plsdof
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Degrees of Freedom and Statistical Inference for Partial Least Squares Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
The plsdof package provides Degrees of Freedom estimates for Partial Least
Squares (PLS) Regression. Model selection for PLS is based on various
information criteria (aic, bic, gmdl) or on cross-validation. Estimates
for the mean and covariance of the PLS regression coefficients are
available. They allow the construction of approximate confidence intervals
and the application of test procedures. Further, cross-validation
procedures for Ridge Regression and Principal Components Regression are

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
%doc %{rlibdir}/plsdof/html
%doc %{rlibdir}/plsdof/DESCRIPTION
%{rlibdir}/plsdof/NAMESPACE
%{rlibdir}/plsdof/R
%{rlibdir}/plsdof/Meta
%{rlibdir}/plsdof/help
%{rlibdir}/plsdof/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora