%global packname  satin
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Functions for reading and displaying satellite data for oceanographic applications with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-hdf5 R-maptools R-maps R-PBSmapping R-chron R-plotrix 


BuildRequires:    R-devel tex(latex) R-hdf5 R-maptools R-maps R-PBSmapping R-chron R-plotrix



%description
Main functions extract a user defined subset of satellite data from hdf5
files which are then available for further analyses and can also be
displayed in maps. Currently supported NOAA products includes: Advanced
Very High Resolution Radiometer (AVHRR); Quick Scatterometer (QuikSCAT);
Moderate-resolution Imaging Spectroradiometer (from Aqua satellite: Aqua
MODIS) and Sea-viewing Wide Field-of-view Sensor (SeaWiFS). The functions
have been tested with sea surface temperature (SST) from AVHRR and Aqua
MODIS; chlorophyll-a (Chl-a) concentration from Aqua MODIS and SeaWiFS and
ocean surface wind speed data from QuikSCAT.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora