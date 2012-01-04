%global packname  care
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          High-Dimensional Regression and CAR Score Variable Selection

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-corpcor 

BuildRequires:    R-devel tex(latex) R-corpcor 

%description
The "care" package implements the regression approach of Zuber and
Strimmer (2011) "High-dimensional regression and variable selection using
CAR scores" SAGMB 10: 34. CAR scores measure the correlation between the
response and the Mahalanobis-decorrelated predictors.  The squared CAR
score is a natural measure of variable importance and provides a canonical
ordering of variables. This package provides functions for estimating CAR
scores, for variable selection using CAR scores, and for estimating
corresponding regression coefficients. Both shrinkage as well as empirical
estimators are available.

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
%doc %{rlibdir}/care/NEWS
%doc %{rlibdir}/care/html
%doc %{rlibdir}/care/DESCRIPTION
%{rlibdir}/care/LICENSE
%{rlibdir}/care/Meta
%{rlibdir}/care/R
%{rlibdir}/care/data
%{rlibdir}/care/help
%{rlibdir}/care/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora