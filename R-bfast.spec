%global packname  bfast
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          BFAST: Breaks For Additive Seasonal and Trend

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-strucchange R-MASS R-forecast 

BuildRequires:    R-devel tex(latex) R-strucchange R-MASS R-forecast 

%description
BFAST integrates the decomposition of time series into trend, seasonal,
and remainder components with methods for detecting and characterizing
abrupt changes within the trend and seasonal components. BFAST can be used
to analyze different types of satellite image time series and can be
applied to other disciplines dealing with seasonal or non-seasonal time
series, such as hydrology, climatology, and econometrics. The algorithm
can be extended to label detected changes with information on the
parameters of the fitted piecewise linear models.

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
%doc %{rlibdir}/bfast/CITATION
%doc %{rlibdir}/bfast/DESCRIPTION
%doc %{rlibdir}/bfast/html
%{rlibdir}/bfast/INDEX
%{rlibdir}/bfast/data
%{rlibdir}/bfast/R
%{rlibdir}/bfast/NAMESPACE
%{rlibdir}/bfast/Meta
%{rlibdir}/bfast/help

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora