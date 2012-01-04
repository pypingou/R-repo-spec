%global packname  DistributionUtils
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Distribution Utilities

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains utilities which are of use in the packages I have
developed for dealing with distributions. Currently these packages are
GeneralizedHyperbolic, VarianceGamma, and SkewHyperbolic. Additional
packages are under development. Each of these packages requires
DistributionUtils. Functionality includes sample skewness and kurtosis,
log-histogram, tail plots, moments by integration, changing the point
about which a moment is calculated, functions for testing distributions
using inversion tests and the Massart inequality. Also includes an
implementation of the incomplete Bessel K function.

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
%doc %{rlibdir}/DistributionUtils/html
%doc %{rlibdir}/DistributionUtils/NEWS
%doc %{rlibdir}/DistributionUtils/DESCRIPTION
%{rlibdir}/DistributionUtils/unitTests
%{rlibdir}/DistributionUtils/Meta
%{rlibdir}/DistributionUtils/libs
%{rlibdir}/DistributionUtils/help
%{rlibdir}/DistributionUtils/NAMESPACE
%{rlibdir}/DistributionUtils/INDEX
%{rlibdir}/DistributionUtils/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora