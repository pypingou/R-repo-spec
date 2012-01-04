%global packname  htSeqTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Quality Control, Visualization and Processing for High-Throughput Sequencing data

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-IRanges R-methods R-MASS R-BSgenome R-GenomicRanges 


BuildRequires:    R-devel tex(latex) R-Biobase R-IRanges R-methods R-MASS R-BSgenome R-GenomicRanges



%description
We provide efficient, easy-to-use tools for High-Throughput Sequencing
(ChIP-seq, RNAseq etc.). These include MDS plots (analogues to PCA),
detecting inefficient immuno-precipitation or over-amplification
artifacts, tools to identify and test for genomic regions with large
accumulation of reads, and visualization of coverage profiles.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora