%global packname  demography
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.10
Release:          1%{?dist}
Summary:          Forecasting mortality, fertility, migration and population data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-forecast R-rainbow R-ftsa 

BuildRequires:    R-devel tex(latex) R-forecast R-rainbow R-ftsa 

%description
Functions for demographic analysis including lifetable calculations;
Lee-Carter modelling; functional data analysis of mortality rates,
fertility rates, net migration numbers; and stochastic population

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10-1
- initial package for Fedora