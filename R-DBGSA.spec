%global packname  DBGSA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          methods of distance-based gene set functional enrichment analysis.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fdrtool 

BuildRequires:    R-devel tex(latex) R-fdrtool 

%description
This package provides methods and examples to support a method of Gene Set
Functional Enrichment Analysis (GSFEA). DBGSA is a novel distance-based
gene set enrichment analysis method. We consider that, the distance
between 2 groups with different phenotype by focusing on the gene
expression should be larger, if a certain gene functional set was
significantly associated with a particular phenotype.

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
%doc %{rlibdir}/DBGSA/html
%doc %{rlibdir}/DBGSA/DESCRIPTION
%{rlibdir}/DBGSA/R
%{rlibdir}/DBGSA/Meta
%{rlibdir}/DBGSA/help
%{rlibdir}/DBGSA/data
%{rlibdir}/DBGSA/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora