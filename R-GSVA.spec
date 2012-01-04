%global packname  GSVA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Gene Set Variation Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Gene Set Variation Analysis (GSVA) is a non-parametric, unsupervised
method for estimating variation of gene set enrichment through the samples
of a expression data set. GSVA performs a change in coordinate systems,
transforming the data from a gene by sample matrix to a gene-set by sample
matrix, thereby allowing the evaluation of pathway enrichment for each
sample. This new matrix of GSVA enrichment scores facilitates applying
standard analytical methods like functional enrichment, survival analysis,
clustering, CNV-pathway analysis or cross-tissue pathway analysis, in a
pathway-centric manner. Users on all platforms must install the GNU
Scientific Library; see the README file, available in the source
distribution of this file, for details.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora