%global packname  smoothSurv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Survival Regression with Smoothed Error Distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
This package contains primarily a function to fit a regression model with
possibly right, left or interval censored observations and with the error
distrbution expressed as a mixture of G-splines. Core part of the
computation is done in compiled C++ written using the Scythe Statistical
Libary Version 0.3.

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
%doc %{rlibdir}/smoothSurv/html
%doc %{rlibdir}/smoothSurv/DESCRIPTION
%doc %{rlibdir}/smoothSurv/doc
%{rlibdir}/smoothSurv/libs
%{rlibdir}/smoothSurv/R
%{rlibdir}/smoothSurv/INDEX
%{rlibdir}/smoothSurv/help
%{rlibdir}/smoothSurv/Meta
%{rlibdir}/smoothSurv/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora