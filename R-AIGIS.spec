%global packname  AIGIS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Areal Interpolation for GIS data

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gpclib 

BuildRequires:    R-devel tex(latex) R-gpclib 

%description
AIGIS can be used to interpolate spatially associated data onto arbitrary
target polygons which lack such data.  Version 1.0 of the package is
oriented toward convenient interpolation of specific US census data for
California, but the tools provided should work for any combination of GIS
data source and target polygon, provided appropriate care is taken. 
Future versions will be aimed at facilitating more general applications.

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
%doc %{rlibdir}/AIGIS/html
%doc %{rlibdir}/AIGIS/DESCRIPTION
%{rlibdir}/AIGIS/R
%{rlibdir}/AIGIS/Meta
%{rlibdir}/AIGIS/help
%{rlibdir}/AIGIS/data
%{rlibdir}/AIGIS/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora