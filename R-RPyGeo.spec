%global packname  RPyGeo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          ArcGIS Geoprocessing in R via Python

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-shapefiles R-RSAGA 


BuildRequires:    R-devel tex(latex) R-shapefiles R-RSAGA



%description
Provide access to (virtually any) ArcGIS Geoprocessing tool from within R
by running Python geoprocessing scripts without writing Python code or
touching ArcGIS. Requires ArcGIS >=9.2, a suitable version of Python (for
ArcGIS 9.2: Python 2.4; for ArcGIS 10.0: 2.6), and Windows.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3-1
- initial package for Fedora