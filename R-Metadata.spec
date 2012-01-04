%global packname  Metadata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Collates Metadata for Climate Surface Stations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-raster R-sp R-ncdf R-rgdal R-RCurl 
Requires:         R-R.utils 

BuildRequires:    R-devel tex(latex) R-raster R-sp R-ncdf R-rgdal R-RCurl
BuildRequires:    R-R.utils 


%description
This package collects and downloads a variety of open GIS datasets that
can be used to characterize the surface properties of Latitude/Longitude
points. In addition, some restricted ( registration required to download)
datasets are processed. Dataset include: distance from coast, disatnce
from airport, land cover, land use, population density, historical
populations, nightlights, impermable surfaces,urban extent, irrigation,
and blue water use.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora