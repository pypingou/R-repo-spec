%global packname  ggmap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          A package for spatial visualization with Google Maps and OpenStreetMap

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RgoogleMaps R-ReadImages R-ggplot2 R-plyr R-reshape2 

BuildRequires:    R-devel tex(latex) R-RgoogleMaps R-ReadImages R-ggplot2 R-plyr R-reshape2 

%description
ggmap allows the the easy visualization of spatial data and models on top
of Google Maps or OpenStreetMaps using ggplot2.

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
* Wed Dec 07 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora