%global packname  TSA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.98
Release:          1%{?dist}
Summary:          Time Series Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-leaps R-locfit R-mgcv R-tseries 


BuildRequires:    R-devel tex(latex) R-leaps R-locfit R-mgcv R-tseries



%description
Contains R functions and datasets detailed in the book "Time Series
Analysis with Applications in R (second edition)" by Jonathan Cryer and
Kung-Sik Chan

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.98-1
- initial package for Fedora