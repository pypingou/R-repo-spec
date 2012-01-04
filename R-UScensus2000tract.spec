%global packname  UScensus2000tract
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.03
Release:          1%{?dist}
Summary:          US Census 2000 Tract Level Shapefiles and Additional Demographic Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-maptools R-sp R-foreign R-methods R-grDevices R-base R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-maptools R-sp R-foreign R-methods R-grDevices R-base R-stats R-utils 

%description
US 2000 Census Tract shapefiles and additional demographic data from the
SF1 100 percent files. This data set contains polygon files in lat/lon
coordinates and the corresponding demographic data for a number of
different variables.

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
%doc %{rlibdir}/UScensus2000tract/html
%doc %{rlibdir}/UScensus2000tract/DESCRIPTION
%{rlibdir}/UScensus2000tract/Meta
%{rlibdir}/UScensus2000tract/help
%{rlibdir}/UScensus2000tract/data
%{rlibdir}/UScensus2000tract/INDEX
%{rlibdir}/UScensus2000tract/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.03-1
- initial package for Fedora