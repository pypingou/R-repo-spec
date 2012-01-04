%global packname  geoPlot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Performs Address Comparison

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package uses 2 separate algorithms to perform address comparison. 
The first concatenates the numerical portion of the address to the postal
code and the second utilizes the Google Maps API to resolve latitude and
longitude then compares them by implementing the haversine formula for
geospatial distance.

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
%doc %{rlibdir}/geoPlot/doc
%doc %{rlibdir}/geoPlot/html
%doc %{rlibdir}/geoPlot/DESCRIPTION
%{rlibdir}/geoPlot/help
%{rlibdir}/geoPlot/INDEX
%{rlibdir}/geoPlot/Meta
%{rlibdir}/geoPlot/R
%{rlibdir}/geoPlot/data
%{rlibdir}/geoPlot/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora