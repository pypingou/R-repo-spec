%global packname  sem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Structural Equation Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-MASS R-matrixcalc 


BuildRequires:    R-devel tex(latex) R-stats R-MASS R-matrixcalc



%description
This package contains functions for fitting general linear structural
equation models (with observed and unobserved variables) using the RAM
approach, and for fitting structural equations in observed-variable models
by two-stage least squares.

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
%doc %{rlibdir}/sem/NEWS
%doc %{rlibdir}/sem/DESCRIPTION
%doc %{rlibdir}/sem/html
%{rlibdir}/sem/Meta
%{rlibdir}/sem/help
%{rlibdir}/sem/INDEX
%{rlibdir}/sem/R
%{rlibdir}/sem/data
%{rlibdir}/sem/CHANGES
%{rlibdir}/sem/NAMESPACE
%{rlibdir}/sem/etc

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.1-1
- initial package for Fedora