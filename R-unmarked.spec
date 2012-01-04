%global packname  unmarked
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Models for Data from Unmarked Animals

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-reshape R-lattice R-Rcpp R-RcppArmadillo 
Requires:         R-graphics R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-reshape R-lattice R-Rcpp R-RcppArmadillo
BuildRequires:    R-graphics R-stats R-utils 


%description
Unmarked fits hierarchical models of animal abundance and occurrence to
data collected using survey methods such as point counts, site occupancy
sampling, distance sampling, removal sampling, and double observer
sampling. Parameters governing the state and observation processes can be
modeled as functions of covariates.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3-1
- initial package for Fedora