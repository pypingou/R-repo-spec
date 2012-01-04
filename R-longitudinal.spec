%global packname  longitudinal
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Analysis of Multiple Time Course Data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-corpcor 

BuildRequires:    R-devel tex(latex) R-corpcor 

%description
This package contains general data structures and functions for
longitudinal data with multiple variables, repeated measurements, and
irregularly spaced time points. It also implements a shrinkage estimator
of dynamical correlation and dynamical covariance.

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
%doc %{rlibdir}/longitudinal/NEWS
%doc %{rlibdir}/longitudinal/COPYING
%doc %{rlibdir}/longitudinal/html
%doc %{rlibdir}/longitudinal/DESCRIPTION
%{rlibdir}/longitudinal/INDEX
%{rlibdir}/longitudinal/help
%{rlibdir}/longitudinal/data
%{rlibdir}/longitudinal/Meta
%{rlibdir}/longitudinal/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.6-1
- initial package for Fedora