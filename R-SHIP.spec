%global packname  SHIP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          SHrinkage covariance Incorporating Prior knowledge

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The SHIP-package allows the estimation of various types of shrinkage
covariance matrices. These types differ in terms of the so-called
covariance target (to be chosen by the user), the highly structured matrix
which the standard unbiased sample covariance matrix is shrunken towards
and which optionally incorporates prior biological knowledge extracted
from the database KEGG. The shrinkage intensity is obtained via an
analytical procedure.

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
%doc %{rlibdir}/SHIP/html
%doc %{rlibdir}/SHIP/DESCRIPTION
%{rlibdir}/SHIP/help
%{rlibdir}/SHIP/INDEX
%{rlibdir}/SHIP/Meta
%{rlibdir}/SHIP/data
%{rlibdir}/SHIP/R
%{rlibdir}/SHIP/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora