%global packname  ChIPpeakAnno
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Batch annotation of the peaks identified from either ChIP-seq, ChIP-chip experiments or any experiments resulted in large number of chromosome ranges.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-biomaRt R-multtest R-IRanges R-Biostrings R-BSgenome R-BSgenome.Ecoli.NCBI.20080805 R-GO.db R-org.Hs.eg.db R-limma R-gplots 
Requires:         R-gplots R-biomaRt R-multtest R-IRanges R-Biostrings R-BSgenome R-GO.db R-limma R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-biomaRt R-multtest R-IRanges R-Biostrings R-BSgenome R-BSgenome.Ecoli.NCBI.20080805 R-GO.db R-org.Hs.eg.db R-limma R-gplots
BuildRequires:    R-gplots R-biomaRt R-multtest R-IRanges R-Biostrings R-BSgenome R-GO.db R-limma R-AnnotationDbi 


%description
The package includes functions to retrieve the sequences around the peak,
obtain enriched Gene Ontology (GO) terms, find the nearest gene, exon,
miRNA or custom features such as most conserved elements and other
transcription factor binding sites supplied by users. Starting 2.0.5, new
functions have been added for finding the peaks with bi-directional
promoters with summary statistics (peaksNearBDP), for summarizing the
occurrence of motifs in peaks (summarizePatternInPeaks) and for adding
other IDs to annotated peaks or enrichedGO (addGeneIDs). This package
leverages the biomaRt, IRanges, Biostrings, BSgenome, GO.db, multtest and
stat packages

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.0-1
- initial package for Fedora