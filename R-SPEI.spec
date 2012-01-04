%global packname  SPEI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Calculation of the Standardised Precipitation-Evapotranspiration Index

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lmomco 

BuildRequires:    R-devel tex(latex) R-lmomco 

%description
A set of functions for computing potential evapotranspiration and several
widely used drought indices including the Standardized
Precipitation-Evapotranspiration Index (SPEI).

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
%doc %{rlibdir}/SPEI/html
%doc %{rlibdir}/SPEI/DESCRIPTION
%{rlibdir}/SPEI/R
%{rlibdir}/SPEI/data
%{rlibdir}/SPEI/help
%{rlibdir}/SPEI/INDEX
%{rlibdir}/SPEI/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora