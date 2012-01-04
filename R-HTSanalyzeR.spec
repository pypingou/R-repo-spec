%global packname  HTSanalyzeR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.0
Release:          1%{?dist}
Summary:          Gene set over-representation, enrichment and network analyses for high-throughput screens

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-igraph R-GSEABase R-BioNet R-cellHTS2 R-RankProd R-methods 

BuildRequires:    R-devel tex(latex) R-igraph R-GSEABase R-BioNet R-cellHTS2 R-RankProd R-methods 

%description
This package provides classes and methods for gene set
over-representation, enrichment and network analyses on high-throughput
screens. The over-representation analysis is performed based on
hypergeometric tests. The enrichment analysis is based on the GSEA
algorithm (Subramanian et al. PNAS 2005). The network analysis identifies
enriched subnetworks based on algorithms from the BioNet package (Beisser
et al., Bioinformatics 2010). A pipeline is also specifically designed for
cellHTS2 object to perform integrative network analyses of high-throughput
RNA interference screens. The users can build their own analysis pipeline
for their own data set based on this package.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.0-1
- initial package for Fedora