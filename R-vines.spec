%global packname  vines
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Multivariate Dependence Modeling with Vines

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-copula R-ADGofTest R-cubature R-TSP 

BuildRequires:    R-devel tex(latex) R-methods R-copula R-ADGofTest R-cubature R-TSP 

%description
Vines are graphical models for pair-copula constructions that allow
building high-dimensional distributions using bivariate copulas and
marginal density functions. This package contains S4 classes for vines
(C-vines and D-vines) and methods for inference, goodness-of-fit tests,
density evaluation, distribution function evaluation, and simulation.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora