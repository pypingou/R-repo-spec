%global packname  ergm.userterms
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          User-specified terms for the statnet suite of packages

Group:            Applications/Engineering 
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-network R-ergm 

BuildRequires:    R-devel tex(latex) R-network R-ergm 

%description
A template package to demonstrate the use of user-specified statistics for
use in "ergm" models as part of the "statnet" suite of packages.

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
%doc %{rlibdir}/ergm.userterms/DESCRIPTION
%doc %{rlibdir}/ergm.userterms/html
%doc %{rlibdir}/ergm.userterms/doc
%doc %{rlibdir}/ergm.userterms/CITATION
%{rlibdir}/ergm.userterms/INDEX
%{rlibdir}/ergm.userterms/LICENSE
%{rlibdir}/ergm.userterms/NAMESPACE
%{rlibdir}/ergm.userterms/R
%{rlibdir}/ergm.userterms/libs
%{rlibdir}/ergm.userterms/help
%{rlibdir}/ergm.userterms/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora