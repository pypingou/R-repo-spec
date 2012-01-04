%global packname  SAFD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Statistical Analysis of Fuzzy Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The aim of the package is to provide some basic functions for doing
statistics with one dimensional Fuzzy Data (in the form of polygonal fuzzy
numbers). In particular, the package contains functions for the basic
operations on the class of fuzzy numbers (sum, scalar product, mean,
Hukuhara difference, quantiles) as well as for calculating (Bertoluzza)
distance, sample variance, sample covariance, sample correlation, and the
Dempster-Shafer (levelwise) histogram. Moreover a function to simulate
fuzzy random variables, bootstrap tests for the equality of means, and a
function to do linear regression given trapezoidal fuzzy data is included.
Version 0.3 fixes some bugs of version 0.2 and includes an additional
function to calculate quantiles of samples of polygonal fuzzy numbers.

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
%doc %{rlibdir}/SAFD/html
%doc %{rlibdir}/SAFD/DESCRIPTION
%{rlibdir}/SAFD/Meta
%{rlibdir}/SAFD/data
%{rlibdir}/SAFD/R
%{rlibdir}/SAFD/NAMESPACE
%{rlibdir}/SAFD/help
%{rlibdir}/SAFD/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora