%global packname  expsmooth
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.01
Release:          1%{?dist}
Summary:          Data sets from "Forecasting with exponential smoothing"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats R-tseries R-forecast 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-tseries R-forecast 

%description
Data sets from the book "Forecasting with exponential smoothing: the state
space approach" by Hyndman, Koehler, Ord and Snyder (Springer, 2008).

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
%doc %{rlibdir}/expsmooth/DESCRIPTION
%doc %{rlibdir}/expsmooth/html
%{rlibdir}/expsmooth/R
%{rlibdir}/expsmooth/INDEX
%{rlibdir}/expsmooth/NAMESPACE
%{rlibdir}/expsmooth/help
%{rlibdir}/expsmooth/Meta
%{rlibdir}/expsmooth/data

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.01-1
- initial package for Fedora