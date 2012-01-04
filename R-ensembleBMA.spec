%global packname  ensembleBMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          5.0.2
Release:          1%{?dist}
Summary:          Probabilistic Forecasting using Ensembles and Bayesian Model Averaging

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-chron 

BuildRequires:    R-devel tex(latex) R-chron 

%description
Bayesian Model Averaging to create probabilistic forecasts from ensemble
forecasts and weather observations.

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
%doc %{rlibdir}/ensembleBMA/html
%doc %{rlibdir}/ensembleBMA/DESCRIPTION
%{rlibdir}/ensembleBMA/INDEX
%{rlibdir}/ensembleBMA/help
%{rlibdir}/ensembleBMA/R
%{rlibdir}/ensembleBMA/Meta
%{rlibdir}/ensembleBMA/NAMESPACE
%{rlibdir}/ensembleBMA/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.0.2-1
- initial package for Fedora