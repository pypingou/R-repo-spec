%global packname  pasilla
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.10
Release:          1%{?dist}
Summary:          Data package with per-exon and per-gene read counts of RNA-seq samples of Pasilla knock-down by Brooks et al., Genome Reaearch 2011.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides per-exon and per-gene read counts computed for
selected genes from RNA-seq data that were presented in the article
"Conservation of an RNA regulatory map between Drosophila and mammals" by
Brooks AN, Yang L, Duff MO, Hansen KD, Park JW, Dudoit S, Brenner SE,
Graveley BR, Genome Res. 2011 Feb;21(2):193-202, Epub 2010 Oct 4, PMID:
20921232.  The experiment studied the effect of RNAi knockdown of Pasilla,
the Drosophila melanogaster ortholog of mammalian NOVA1 and NOVA2, on the
transcriptome.  The package vignette describes how the data provided here
were derived from the RNA-Seq read sequence data that is provided by NCBI
Gene Expression Omnibus under accession numbers GSM461176 to GSM461181

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.10-1
- initial package for Fedora