%global packname  tolerance
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Functions for calculating tolerance intervals

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rgl R-stats4 


BuildRequires:    R-devel tex(latex) R-rgl R-stats4



%description
Tolerance limits provide the limits between which we can expect to find a
specified proportion of a population with a given level of confidence. 
This package provides functions for estimating tolerance limits for
various distributions.  Plotting is also available for tolerance limits of
continuous random variables.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora