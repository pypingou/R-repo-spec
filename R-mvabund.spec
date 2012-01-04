%global packname  mvabund
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          statistical methods for analysing multivariate abundance data

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Rcpp 


BuildRequires:    R-devel tex(latex) R-methods R-Rcpp



%description
A set of tools for displaying, modeling and analysing multivariate
abundance data in community ecology. See mvabund-package.Rd for details of
overall package organization. The package is implemented with the Gnu
Scientific Library (http://www.gnu.org/software/gsl/) and Rcpp
(http://dirk.eddelbuettel.com/code/rcpp.html) R / C++ classes.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora