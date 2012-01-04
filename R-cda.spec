%global packname  cda
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Coupled dipole approximation

Group:            Applications/Engineering 
License:          GPL (>= 2) + file LICENCE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Rcpp R-RcppArmadillo R-plyr R-ggplot2 R-statmod R-randtoolbox 

BuildRequires:    R-devel tex(latex) R-methods R-Rcpp R-RcppArmadillo R-plyr R-ggplot2 R-statmod R-randtoolbox 

%description
Given a set of ellipsoidal nanoparticles (positions and sizes), calculates
the polarizability tensor for the dipoles associated with each particle,
and solves the coupled-dipole equations by direct inversion of the
interaction matrix. Retardation is included in the interaction.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora