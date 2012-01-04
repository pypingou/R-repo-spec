%global packname  dbstats
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Distance-based statistics (dbstats)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster R-pls 

BuildRequires:    R-devel tex(latex) R-cluster R-pls 

%description
This package contains functions for distance-based prediction methods.
These are methods for prediction where predictor information is coded as a
matrix of distances between individuals. Distances can either be directly
input as an interdistances matrix, a squared interdistances matrix, an
inner-products matrix or computed from observed explanatory variables.

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
%doc %{rlibdir}/dbstats/DESCRIPTION
%doc %{rlibdir}/dbstats/html
%{rlibdir}/dbstats/help
%{rlibdir}/dbstats/Meta
%{rlibdir}/dbstats/R
%{rlibdir}/dbstats/INDEX
%{rlibdir}/dbstats/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora