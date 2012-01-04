%global packname  fpp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Data sets for the "Forecasting: principles and practice" workshop by Rob J Hyndman, June 2011

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats R-tseries R-forecast R-fma R-expsmooth 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-tseries R-forecast R-fma R-expsmooth 

%description
All data sets required for the workshop in Kandersteg, Switzerland, 20-22
June 2011.

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
%doc %{rlibdir}/fpp/html
%doc %{rlibdir}/fpp/DESCRIPTION
%{rlibdir}/fpp/R
%{rlibdir}/fpp/data
%{rlibdir}/fpp/NAMESPACE
%{rlibdir}/fpp/INDEX
%{rlibdir}/fpp/Meta
%{rlibdir}/fpp/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora