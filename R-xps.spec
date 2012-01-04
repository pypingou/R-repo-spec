%global packname  xps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          Processing and Analysis of Affymetrix Oligonucleotide Arrays including Exon Arrays, Whole Genome Arrays and Plate Arrays

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The package handles pre-processing, normalization, filtering and analysis
of Affymetrix GeneChip expression arrays, including exon arrays (Exon 1.0
ST: core, extended, full probesets), gene arrays (Gene 1.0 ST) and plate
arrays on computers with 1 GB RAM only. It imports Affymetrix .CDF, .CLF,
.PGF and .CEL as well as annotation files, and computes e.g. RMA, MAS5,
FARMS, DFW, FIRMA, tRMA, MAS5-calls, DABG-calls, I/NI-calls. It is an R
wrapper to XPS (eXpression Profiling System), which is based on ROOT, an
object-oriented framework developed at CERN. Thus, the prior installation
of ROOT is a prerequisite for the usage of this package, however, no
knowledge of ROOT is required. ROOT is licensed under LGPL and can be
downloaded from http://root.cern.ch.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora