%global packname  RMAWGEN
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          RMAWGEN (R Multi-site Auto-regressive Weather GENeretor): a package to generate daily time series from monthly mean values

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-chron R-date R-vars R-MASS R-strucchange R-urca R-lmtest R-sandwich 

BuildRequires:    R-devel tex(latex) R-chron R-date R-vars R-MASS R-strucchange R-urca R-lmtest R-sandwich 

%description
This package contains S3 functions for spatial multi-site stochastic
generation of daily timeseries of temperature and precipitation. The
implemented tools make use of Vectorial AutoRegressive models (VARs). The
VAR is calibrated by daily instrumental timeseries given and then works
with monthly timeseries as input. Bugs/comments/questions/collaboration of
any kind are warmly welcomed.

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
%doc %{rlibdir}/RMAWGEN/html
%doc %{rlibdir}/RMAWGEN/DESCRIPTION
%{rlibdir}/RMAWGEN/help
%{rlibdir}/RMAWGEN/NAMESPACE
%{rlibdir}/RMAWGEN/Meta
%{rlibdir}/RMAWGEN/R
%{rlibdir}/RMAWGEN/data
%{rlibdir}/RMAWGEN/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora