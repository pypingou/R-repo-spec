%global packname  fda.usc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.5
Release:          1%{?dist}
Summary:          Functional Data Analysis and Utilities for Statistical Computing (fda.usc)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fda R-splines R-MASS R-mgcv R-e1071 R-pls 

BuildRequires:    R-devel tex(latex) R-fda R-splines R-MASS R-mgcv R-e1071 R-pls 

%description
This package implements functional data methods.

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
%doc %{rlibdir}/fda.usc/NEWS
%doc %{rlibdir}/fda.usc/html
%doc %{rlibdir}/fda.usc/DESCRIPTION
%{rlibdir}/fda.usc/INDEX
%{rlibdir}/fda.usc/Meta
%{rlibdir}/fda.usc/R
%{rlibdir}/fda.usc/data
%{rlibdir}/fda.usc/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.5-1
- initial package for Fedora