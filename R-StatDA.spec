%global packname  StatDA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Statistical Analysis for Environmental Data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-akima R-car R-cluster R-e1071 R-class R-geoR R-sp R-leaps R-MASS R-pixmap R-robustbase R-rgl R-mgcv R-methods 


BuildRequires:    R-devel tex(latex) R-akima R-car R-cluster R-e1071 R-class R-geoR R-sp R-leaps R-MASS R-pixmap R-robustbase R-rgl R-mgcv R-methods



%description
This package offers different possibilities to make statistical analysis
for Environmental Data.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora