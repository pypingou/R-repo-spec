%global packname  RghcnV3
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.5
Release:          1%{?dist}
Summary:          Global Historical Climate Network Version 3

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.utils R-R.oo R-R.methodsS3 R-zoo R-raster R-sp R-ncdf R-corpcor 


BuildRequires:    R-devel tex(latex) R-R.utils R-R.oo R-R.methodsS3 R-zoo R-raster R-sp R-ncdf R-corpcor



%description
The Rghcn package provides the core functions required to download and
format the GHCN V3 data and process it into temperature series and
temperature anomaly series. The data is reformated so that integration
with objects in the system is straightforward. In addition, there are core
functions required to download and create land masks and functions to
download and import Sea Surface Temperature (SST) data.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.5-1
- initial package for Fedora