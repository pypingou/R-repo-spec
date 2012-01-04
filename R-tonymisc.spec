%global packname  tonymisc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Functions for Econometrics Output

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-memisc R-AER R-car R-nlme 

BuildRequires:    R-devel tex(latex) R-memisc R-AER R-car R-nlme 

%description
This package provides several methods and functions that simplify output
from regression packages.

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
%doc %{rlibdir}/tonymisc/DESCRIPTION
%doc %{rlibdir}/tonymisc/html
%{rlibdir}/tonymisc/NAMESPACE
%{rlibdir}/tonymisc/Meta
%{rlibdir}/tonymisc/data
%{rlibdir}/tonymisc/INDEX
%{rlibdir}/tonymisc/R
%{rlibdir}/tonymisc/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora