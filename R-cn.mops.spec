%global packname  cn.mops
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          cn.mops - Mixture of Poisson for CNV detection in NGS data

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-IRanges R-GenomicRanges 

BuildRequires:    R-devel tex(latex) R-Biobase R-IRanges R-GenomicRanges 

%description
cn.mops (Copy Number estimation by a Mixture Of PoissonS) is a data
processing pipeline for copy number variations and aberrations (CNVs and
CNAs) from next generation sequencing (NGS) data. The package supplies
functions to convert BAM files into read count matrices or genomic ranges
objects, which are the input objects for cn.mops. cn.mops models the
depths of coverage across samples at each genomic position. Therefore, it
does not suffer from read count biases along chromosomes. Using a Bayesian
approach, cn.mops decomposes read variations across samples into integer
copy numbers and noise by its mixture components and Poisson
distributions, respectively. cn.mops guarantees a low FDR because wrong
detections are indicated high noise and filtered out. cn.mops is very fast
and written in C++.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora