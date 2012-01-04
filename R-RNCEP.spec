%global packname  RNCEP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Obtain, organize, and visualize NCEP weather data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-abind R-maps R-fields R-tgp R-fossil R-tcltk 

BuildRequires:    R-devel tex(latex) R-abind R-maps R-fields R-tgp R-fossil R-tcltk 

%description
This package contains functions to retrieve, organize, and visualize
weather data from the NCEP/NCAR Reanalysis and NCEP/DOE Reanalysis II
datasets.  Data are queried via the Internet and may be obtained for a
specified spatial and temporal extent or interpolated to a point in space
and time. We also provide functions to visualize these weather data on a

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
%doc %{rlibdir}/RNCEP/DESCRIPTION
%doc %{rlibdir}/RNCEP/html
%doc %{rlibdir}/RNCEP/CITATION
%{rlibdir}/RNCEP/R
%{rlibdir}/RNCEP/Meta
%{rlibdir}/RNCEP/INDEX
%{rlibdir}/RNCEP/data
%{rlibdir}/RNCEP/help

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora