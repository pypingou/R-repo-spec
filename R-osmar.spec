%global packname  osmar
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.01
Release:          1%{?dist}
Summary:          Importing and working with OpenStreetMap-Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-01.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML R-RCurl R-sp R-gtools 


BuildRequires:    R-devel tex(latex) R-XML R-RCurl R-sp R-gtools



%description
This package imports the (Spatial and Non-Spatial) Data of OpenStreetMap
into objects of R by using the OSM-API v0.6. For now it is reduced on
using various commands of type "GET", like getting data of an explicit
element or a region defined by coordinates. It also includes some methods
on working with the newly created objects.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.01-1
- initial package for Fedora