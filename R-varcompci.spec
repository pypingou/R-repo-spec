%global packname  varcompci
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          VARCOMPCI: A Package for Computation of Confidence Intervals for Variance Components of Mixed Models in R.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package compute confidence intervals on individual variances for any
balanced mixed model, involving five or fewer factors according to Burdick
and Graybill (1992) methodology. The package would fit a saturated model
to the data (main effect and interaction terms of all orders) providing an
ANOVA model with Expected Mean Squares (type III). The output will
include: a table showing the confidence interval (CI) and estimate of each
covariance parameter, as well as the method used to compute the CI, the
Expected Mean Square, an ANOVA table showing the degrees of freedom (df),
sums of squares (SS), mean squares (MS), F statistic, and finally AIC and
BIC measures.

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
%doc %{rlibdir}/varcompci/doc
%doc %{rlibdir}/varcompci/html
%doc %{rlibdir}/varcompci/DESCRIPTION
%{rlibdir}/varcompci/NAMESPACE
%{rlibdir}/varcompci/INDEX
%{rlibdir}/varcompci/Meta
%{rlibdir}/varcompci/data
%{rlibdir}/varcompci/R
%{rlibdir}/varcompci/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora