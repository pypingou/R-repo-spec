%global packname  aspace
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          A collection of functions for estimating centrographic statistics and computational geometries for spatial point patterns

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splancs R-Hmisc R-shapefiles 

BuildRequires:    R-devel tex(latex) R-splancs R-Hmisc R-shapefiles 

%description
A collection of functions for computing centrographic statistics (e.g.,
standard distance, standard deviation ellipse, standard deviation box) for
observations taken at point locations. Separate plotting functions have
been developed for each measure. Users interested in writing results to
ESRI shapefiles can do so by using results from aspace functions as inputs
to the convert.to.shapefile and write.shapefile functions in the
shapefiles library. The aspace library was originally conceived to aid in
the analysis of spatial patterns of travel behaviour (see Buliung and
Remmel, 2008). Major changes in the current version include (1) removal of
dependencies on several external libraries (e.g., gpclib, maptools, sp),
(2) the separation of plotting and estimation capabilities, (3) reduction
in the number of functions, and (4) expansion of analytical capabilities
with additional functions for descriptive analysis and visualization
(e.g., standard deviation box, centre of minimum distance, central

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
%doc %{rlibdir}/aspace/DESCRIPTION
%doc %{rlibdir}/aspace/html
%{rlibdir}/aspace/R
%{rlibdir}/aspace/Meta
%{rlibdir}/aspace/data
%{rlibdir}/aspace/INDEX
%{rlibdir}/aspace/help
%{rlibdir}/aspace/NAMESPACE

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0-1
- initial package for Fedora