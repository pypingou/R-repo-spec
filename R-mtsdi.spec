%global packname  mtsdi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Multivariate time series data imputation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-gam R-splines 

BuildRequires:    R-devel tex(latex) R-stats R-gam R-splines 

%description
This is a EM algorithm based method for imputation of missing values in
multivariate normal time series. The imputation algorithm accounts for
both spatial and temporal correlation structures. Temporal patterns can be
modelled using an ARIMA(p,d,q), optionally with seasonal components, a
non-parametric cubic spline or generalised additive models with exogenous
covariates. This algorithm is specially tailored for climate data with
missing measurements from several monitors along a given region.

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
%doc %{rlibdir}/mtsdi/html
%doc %{rlibdir}/mtsdi/DESCRIPTION
%{rlibdir}/mtsdi/INDEX
%{rlibdir}/mtsdi/Meta
%{rlibdir}/mtsdi/R
%{rlibdir}/mtsdi/help
%{rlibdir}/mtsdi/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora