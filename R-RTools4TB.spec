%global packname  RTools4TB
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Data mining of public microarray data through connections to the TranscriptomeBrowser database.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-limma R-methods 


BuildRequires:    R-devel tex(latex) R-Biobase R-limma R-methods



%description
TranscriptomeBrowser (TBrowser) hosts a large collection of
transcriptional signatures (TS)  automatically extracted from the Gene
Expression Omnibus (GEO) database. Each GEO experiment (GSE) was processed
so that a subset of the original expression matrix containing the most
relevant/informative genes was kept and organized into a set of
homogeneous signatures. Each signature was tested for functional 
enrichment using annotations terms obtained from numerous ontologies or
curated databases (Gene Ontology, KEGG, BioCarta, Swiss-Prot, BBID, SMART,
NIH Genetic Association DB, COG/KOG...) using the DAVID knowledgebase. The
RTools4TB package can be used to perform complexe queries to the database.
Thereby, RTools4TB can be helpful (i) to define the biological contexts
(i.e, experiments) in which a set of genes are co-expressed and (ii) to
define their most frequent neighbors. In addition, RTools4TB comes with a
new algoritm, "Density Based Filtering And Markov Clustering" (DBF-MCL),
whose goal is to partition large and noisy datasets. DBF-MCL is a
tree-step adaptative algorithm that (i) find elements located in dense
areas (ie. clusters) (ii) uses selected items to construct a graph and
(iii) performs graph partitioning using MCL. This algorithm is implemented
in the RTools4TB package although it requires a UNIX-like systems.

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
%doc %{rlibdir}/RTools4TB/html
%doc %{rlibdir}/RTools4TB/DESCRIPTION
%doc %{rlibdir}/RTools4TB/doc
%{rlibdir}/RTools4TB/INDEX
%{rlibdir}/RTools4TB/NAMESPACE
%{rlibdir}/RTools4TB/help
%{rlibdir}/RTools4TB/data
%{rlibdir}/RTools4TB/R
%{rlibdir}/RTools4TB/libs
%{rlibdir}/RTools4TB/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora