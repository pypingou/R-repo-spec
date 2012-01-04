%global packname  FME
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          A Flexible Modelling Environment for Inverse Modelling, Sensitivity, Identifiability, Monte Carlo Analysis.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-deSolve R-rootSolve R-minpack.lm R-MASS R-coda 

BuildRequires:    R-devel tex(latex) R-deSolve R-rootSolve R-minpack.lm R-MASS R-coda 

%description
Provides functions to help in fitting models to data, to perform Monte
Carlo, sensitivity and identifiability analysis. It is intended to work
with models be written as a set of differential equations that are solved
either by an integration routine from package deSolve, or a steady-state
solver from package rootSolve. However, the methods can also be used with
other types of functions.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora