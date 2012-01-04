%global packname  trigger
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Transcriptional Regulatory Inference from Genetics of Gene ExpRession

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-corpcor R-qtl 
Requires:         R-qvalue R-methods R-graphics R-sva 

BuildRequires:    R-devel tex(latex) R-corpcor R-qtl
BuildRequires:    R-qvalue R-methods R-graphics R-sva 


%description
This R package provides tools for the statistical analysis of integrative
genomic data that involve some combination of: genotypes, high-dimensional
intermediate traits (e.g., gene expression, protein abundance), and
higher-order traits (phenotypes). The package includes functions to: (1)
construct global linkage maps between genetic markers and gene expression;
(2) analyze multiple-locus linkage (epistasis) for gene expression; (3)
quantify the proportion of genome-wide variation explained by each locus
and identify eQTL hotspots; (4) estimate pair-wise causal gene regulatory
probabilities and construct gene regulatory networks; and (5) identify
causal genes for a quantitative trait of interest.

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
%doc %{rlibdir}/trigger/html
%doc %{rlibdir}/trigger/DESCRIPTION
%doc %{rlibdir}/trigger/doc
%{rlibdir}/trigger/libs
%{rlibdir}/trigger/Meta
%{rlibdir}/trigger/help
%{rlibdir}/trigger/data
%{rlibdir}/trigger/NAMESPACE
%{rlibdir}/trigger/INDEX
%{rlibdir}/trigger/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora