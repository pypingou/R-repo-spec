%global packname  topGO
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.0
Release:          1%{?dist}
Summary:          topGO: Enrichment analysis for Gene Ontology

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graph R-Biobase R-GO.db R-AnnotationDbi R-SparseM 
Requires:         R-methods R-graph R-Biobase R-SparseM R-AnnotationDbi R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-graph R-Biobase R-GO.db R-AnnotationDbi R-SparseM
BuildRequires:    R-methods R-graph R-Biobase R-SparseM R-AnnotationDbi R-lattice 


%description
topGO package provides tools for testing GO terms while accounting for the
topology of the GO graph. Different test statistics and different methods
for eliminating local similarities and dependencies between GO terms can
be implemented and applied.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.0-1
- initial package for Fedora