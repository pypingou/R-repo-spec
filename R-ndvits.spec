%global packname  ndvits
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          NDVI Time series extraction and analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gstat R-rgdal R-bfast R-RTisean R-RColorBrewer R-lattice 


BuildRequires:    R-devel tex(latex) R-gstat R-rgdal R-bfast R-RTisean R-RColorBrewer R-lattice



%description
The routines extract automatically, for area of interest, Normalized
Difference Vegetation Index (NDVI) time series from different optical
satellite instruments (AVHRR, Spot Vegetation) and to provide tools to
display and analyze the time series.Functions have been developed to study
landscapes and more especially to detect changes in land use land cover.
Phenological metrics can be computed for every season as well as
vegetation anomaly maps.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora