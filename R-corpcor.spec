%global packname  corpcor
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.2
Release:          1%{dist}
Summary:          Efficient Estimation of Covariance and (Partial) Correlation

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements a James-Stein-type shrinkage estimator for the
covariance matrix, with separate shrinkage for variances and correlations.
The details of the method are explained in Sch\"afer and Strimmer (2005)
and Opgen-Rhein and Strimmer (2007).  The approach is both computationally
as well as statistically very efficient, it is applicable to "small n,
large p" data, and always returns a positive definite and well-conditioned
covariance matrix. In addition to inferring the covariance matrix the
package also provides shrinkage estimators for partial correlations and
partial variances. The inverse of the covariance and correlation matrix
can be efficiently computed, as well as any arbitrary power of the
shrinkage correlation matrix.  Furthermore, functions are available for
fast singular value decomposition, for computing the pseudoinverse, and
for checking the rank and positive definiteness of a matrix.

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
%doc %{rlibdir}/corpcor/DESCRIPTION
%doc %{rlibdir}/corpcor/html
%doc %{rlibdir}/corpcor/NEWS
%{rlibdir}/corpcor/help
%{rlibdir}/corpcor/NAMESPACE
%{rlibdir}/corpcor/Meta
%{rlibdir}/corpcor/INDEX
%{rlibdir}/corpcor/R
%{rlibdir}/corpcor/LICENSE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.2-1
- Update to version 1.6.2

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora