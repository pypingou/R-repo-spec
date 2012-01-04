%global packname  costat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Time series costationarity determination and tests of stationarity.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-wavethresh 

BuildRequires:    R-devel tex(latex) R-wavethresh 

%description
Contains functions that can determine whether a time series is
second-order stationary or not (and hence evidence for locally
stationarity). Given two non-stationary series (i.e. locally stationary
series) this package can then discover time-varying linear combinations
that are second-order stationary.

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
%doc %{rlibdir}/costat/html
%doc %{rlibdir}/costat/DESCRIPTION
%{rlibdir}/costat/help
%{rlibdir}/costat/Meta
%{rlibdir}/costat/data
%{rlibdir}/costat/R
%{rlibdir}/costat/NAMESPACE
%{rlibdir}/costat/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora