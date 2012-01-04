%global packname  GeoXp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Interactive exploratory spatial data analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-fields R-KernSmooth R-mvoutlier R-rgl R-robustbase R-spdep R-splancs R-stats R-tcltk 

BuildRequires:    R-devel tex(latex) R-fields R-KernSmooth R-mvoutlier R-rgl R-robustbase R-spdep R-splancs R-stats R-tcltk 

%description
GeoXp is a tool for researchers in spatial statistics, spatial
econometrics, geography, ecology etc allowing to link dynamically
statistical plots with elementary maps. This coupling consists in the fact
that the selection of a zone on the map results in the automatic
highlighting of the corresponding points on the statistical graph or
reversely the selection of a portion of the graph results in the automatic
highlighting of the corresponding points on the map. GeoXp includes tools
from different areas of spatial statistics including geostatistics as well
as spatial econometrics and point processes. Besides elementary plots like
boxplots, histograms or simple scatterplos, GeoXp also couples with maps
Moran scatterplots, variogram cloud, Lorentz Curves,...In order to make
the most of the multidimensionality of the data, GeoXp includes some
dimension reduction techniques such as PCA.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora