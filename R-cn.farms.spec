%global packname  cn.farms
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          cn.farms - Factor Analysis for copy number estimation

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods R-ff R-oligoClasses R-snowfall 
Requires:         R-DBI R-affxparser R-oligo R-DNAcopy R-preprocessCore R-lattice 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods R-ff R-oligoClasses R-snowfall
BuildRequires:    R-DBI R-affxparser R-oligo R-DNAcopy R-preprocessCore R-lattice 


%description
This package implements the cn.FARMS algorithm for copy number variation
(CNV) analysis. cn.FARMS allows to analyze all existing Affymetrix
(10K-SNP6.0) array types, supports high-performance computing using snow
and ff.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora