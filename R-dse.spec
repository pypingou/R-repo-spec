%global packname  dse
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.1
Release:          1%{?dist}
Summary:          Dynamic Systems Estimation (time series package)

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tframe R-setRNG 

BuildRequires:    R-devel tex(latex) R-tframe R-setRNG 

%description
Package dse provides tools for multivariate, linear, time-invariant, time
series models. It includes ARMA and state-space representations, and
methods for converting between them. It also includes simulation methods
and several estimation functions. The package has functions for looking at
model roots, stability, and forecasts at different horizons. The ARMA
model representaion is general, so that VAR, VARX, ARIMA, ARMAX, ARIMAX
can all be considered to be special cases. Kalman filter and smoother
estimates can be obtained from the state space model, and state-space
model reduction techniques are implemented. An introduction and User's
Guide is available in a vignette.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.1-1
- initial package for Fedora