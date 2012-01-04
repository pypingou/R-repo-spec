%global packname  RcmdrPlugin.epack
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Rcmdr plugin for time series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-TeachingDemos R-tseries R-abind R-MASS R-xts R-forecast 


BuildRequires:    R-devel tex(latex) R-Rcmdr R-TeachingDemos R-tseries R-abind R-MASS R-xts R-forecast



%description
This package provides an Rcmdr "plug-in" based on the time series
functions.  Contributors: G. Jay Kerns, John Fox, and Richard Heiberger.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora