%global packname  forecast
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.13
Release:          1%{?dist}
Summary:          Forecasting functions for time series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-tseries R-fracdiff R-zoo 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-tseries R-fracdiff R-zoo 

%description
Methods and tools for displaying and analysing univariate time series
forecasts including exponential smoothing via state space models and
automatic ARIMA modelling.

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
%doc %{rlibdir}/forecast/DESCRIPTION
%doc %{rlibdir}/forecast/html
%{rlibdir}/forecast/data
%{rlibdir}/forecast/libs
%{rlibdir}/forecast/R
%{rlibdir}/forecast/NAMESPACE
%{rlibdir}/forecast/INDEX
%{rlibdir}/forecast/help
%{rlibdir}/forecast/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.13-1
- initial package for Fedora