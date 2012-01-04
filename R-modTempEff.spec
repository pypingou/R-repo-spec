%global packname  modTempEff
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Modelling temperature effects using time series data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mgcv R-splines 

BuildRequires:    R-devel tex(latex) R-mgcv R-splines 

%description
Fits a Constrained Segmented Distributed Lag regression model to
epidemiological time series of mortality, temperature, and other

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
%doc %{rlibdir}/modTempEff/html
%doc %{rlibdir}/modTempEff/DESCRIPTION
%doc %{rlibdir}/modTempEff/CITATION
%doc %{rlibdir}/modTempEff/doc
%{rlibdir}/modTempEff/Meta
%{rlibdir}/modTempEff/data
%{rlibdir}/modTempEff/R
%{rlibdir}/modTempEff/INDEX
%{rlibdir}/modTempEff/NAMESPACE
%{rlibdir}/modTempEff/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora