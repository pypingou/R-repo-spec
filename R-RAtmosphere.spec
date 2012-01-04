%global packname  RAtmosphere
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Standard Atmosperic profiles

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provide an easy way to produce atmospheric profiles of
Pressure, Temperature and Density. It provides also molecular scatter
coeffient for standard atmosphere and for specificated temperature and
pressure profiles.

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
%doc %{rlibdir}/RAtmosphere/html
%doc %{rlibdir}/RAtmosphere/DESCRIPTION
%{rlibdir}/RAtmosphere/INDEX
%{rlibdir}/RAtmosphere/Meta
%{rlibdir}/RAtmosphere/R
%{rlibdir}/RAtmosphere/NAMESPACE
%{rlibdir}/RAtmosphere/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora