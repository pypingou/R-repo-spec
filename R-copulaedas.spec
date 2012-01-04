%global packname  copulaedas
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Estimation of Distribution Algorithms Based on Copula Theory

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-copula R-vines 

BuildRequires:    R-devel tex(latex) R-methods R-copula R-vines 

%description
This package contains implementations of various classes of Estimation of
Distribution Algorithms (EDAs) based on copula theory: Copula EDAs and
Vine EDAs. In this package, EDAs are implemented using S4 classes with
generic functions for its main parts: seeding, selection, learning,
sampling, replacement, local optimization, termination, and reporting. The
package also includes the implementation of a group of well-known
optimization test problems and utility functions to study the behavior of

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
%doc %{rlibdir}/copulaedas/CITATION
%doc %{rlibdir}/copulaedas/DESCRIPTION
%doc %{rlibdir}/copulaedas/NEWS
%doc %{rlibdir}/copulaedas/html
%{rlibdir}/copulaedas/INDEX
%{rlibdir}/copulaedas/NAMESPACE
%{rlibdir}/copulaedas/help
%{rlibdir}/copulaedas/R
%{rlibdir}/copulaedas/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora