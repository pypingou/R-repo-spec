%global packname  schwartz97
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          A package on the Schwartz two-factor commodity model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-FKF R-mvtnorm R-methods 

BuildRequires:    R-devel tex(latex) R-FKF R-mvtnorm R-methods 

%description
This package provides detailed functionality for working with the Schwartz
1997 two-factor commodity model. Essentially, it contains pricing formulas
for futures and European options and the standard d/p/q/r functions for
the distribution of the state variables and futures prices. In addition, a
parameter estimation procedure is contained together with many utilities
as filtering and plotting functionality. This package is accompanied by
futures data of ten commodities.

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
%doc %{rlibdir}/schwartz97/DESCRIPTION
%doc %{rlibdir}/schwartz97/html
%doc %{rlibdir}/schwartz97/doc
%{rlibdir}/schwartz97/data
%{rlibdir}/schwartz97/NAMESPACE
%{rlibdir}/schwartz97/R
%{rlibdir}/schwartz97/Meta
%{rlibdir}/schwartz97/unitTests
%{rlibdir}/schwartz97/INDEX
%{rlibdir}/schwartz97/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.3-1
- initial package for Fedora