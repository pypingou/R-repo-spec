%global packname  LEAPFrOG
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Likelihood Estimation of Admixture in Parents From Offspring Genotypes

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-alabama R-MASS 

BuildRequires:    R-devel tex(latex) R-alabama R-MASS 

%description
Contains LEAPFrOG Gradient Optimisation and Expectation Maximisation
functions for inferring parental admixture proportions from an offspring
with SNP genotypes.

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
%doc %{rlibdir}/LEAPFrOG/COPYING
%doc %{rlibdir}/LEAPFrOG/html
%doc %{rlibdir}/LEAPFrOG/DESCRIPTION
%{rlibdir}/LEAPFrOG/Meta
%{rlibdir}/LEAPFrOG/INDEX
%{rlibdir}/LEAPFrOG/R
%{rlibdir}/LEAPFrOG/help

%changelog
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora