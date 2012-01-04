%global packname  RRF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Regularized Random Forest

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Feature Selection with Regularized Random Forest. This package is based on
the 'randomForest' package by Andy Liaw. The key difference is the RRF
function that builds a regularized random forest.

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
%doc %{rlibdir}/RRF/NEWS
%doc %{rlibdir}/RRF/CITATION
%doc %{rlibdir}/RRF/html
%doc %{rlibdir}/RRF/DESCRIPTION
%{rlibdir}/RRF/NAMESPACE
%{rlibdir}/RRF/Meta
%{rlibdir}/RRF/R
%{rlibdir}/RRF/help
%{rlibdir}/RRF/INDEX
%{rlibdir}/RRF/libs
%{rlibdir}/RRF/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora