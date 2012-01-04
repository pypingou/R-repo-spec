%global packname  rgdal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.5
Release:          1%{?dist}
Summary:          Bindings for the Geospatial Data Abstraction Library

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-sp 


BuildRequires:    R-devel tex(latex) R-methods R-sp



%description
Provides bindings to Frank Warmerdam's Geospatial Data Abstraction Library
(GDAL) (>= 1.3.1) and access to projection/transformation operations from
the PROJ.4 library. The GDAL and PROJ.4 libraries are external to the
package, and, when installing the package from source, must be correctly
installed first. Both GDAL raster and OGR vector map data can be imported
into R, and GDAL raster data and OGR vector data exported. Use is made of
classes defined in the sp package. Windows binaries (including GDAL,
PROJ.4 and Expat) are provided on CRAN. Mac Intel OS X binaries (including
GDAL, PROJ.4 and Expat) are not provided on CRAN, but can be installed
from the CRAN Extras repository with: setRepositories(ind=1:2);

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.5-1
- initial package for Fedora