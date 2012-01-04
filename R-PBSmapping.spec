%global packname  PBSmapping
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.61.9
Release:          1%{?dist}
Summary:          Mapping Fisheries Data and Spatial Analysis Tools

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This software has evolved from fisheries research conducted at the Pacific
Biological Station (PBS) in Nanaimo, British Columbia, Canada. It extends
the R language to include two-dimensional plotting features similar to
those commonly available in a Geographic Information System (GIS). 
Embedded C code speeds algorithms from computational geometry, such as
finding polygons that contain specified point events or converting between
longitude-latitude and Universal Transverse Mercator (UTM) coordinates. 
It includes data for a global shoreline and other data sets in the public
domain. The R directory '.../library/PBSmapping/doc' includes a complete
user's guide PBSmapping-UG.pdf. To use this package effectively, please
consult the guide.

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
%doc %{rlibdir}/PBSmapping/DESCRIPTION
%doc %{rlibdir}/PBSmapping/html
%doc %{rlibdir}/PBSmapping/doc
%{rlibdir}/PBSmapping/Meta
%{rlibdir}/PBSmapping/demo
%{rlibdir}/PBSmapping/libs
%{rlibdir}/PBSmapping/data
%{rlibdir}/PBSmapping/Utils
%{rlibdir}/PBSmapping/R
%{rlibdir}/PBSmapping/NAMESPACE
%{rlibdir}/PBSmapping/help
%{rlibdir}/PBSmapping/INDEX
%{rlibdir}/PBSmapping/Extra

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.61.9-1
- initial package for Fedora