%global packname  MUCflights
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Munich Franz-Josef-Strauss Airport Pattern Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML R-geosphere R-sp R-RSQLite R-NightDay 

BuildRequires:    R-devel tex(latex) R-XML R-geosphere R-sp R-RSQLite R-NightDay 

%description
Functions for downloading flight data from http://www.munich-airport.de
and for analyzing flight patterns.

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
%doc %{rlibdir}/MUCflights/DESCRIPTION
%doc %{rlibdir}/MUCflights/html
%{rlibdir}/MUCflights/NAMESPACE
%{rlibdir}/MUCflights/Meta
%{rlibdir}/MUCflights/help
%{rlibdir}/MUCflights/data
%{rlibdir}/MUCflights/R
%{rlibdir}/MUCflights/MUCflights.RData
%{rlibdir}/MUCflights/INDEX
%{rlibdir}/MUCflights/maps

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.3-1
- initial package for Fedora