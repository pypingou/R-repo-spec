%global packname  genoset
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Provides classes similar to ExpressionSet for copy number analysis

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-IRanges 
Requires:         R-Biobase R-DNAcopy R-graphics R-IRanges R-methods R-stats R-GenomicRanges R-BSgenome R-Biostrings R-bigmemory 

BuildRequires:    R-devel tex(latex) R-Biobase R-IRanges
BuildRequires:    R-Biobase R-DNAcopy R-graphics R-IRanges R-methods R-stats R-GenomicRanges R-BSgenome R-Biostrings R-bigmemory 


%description
Load, manipulate, and plot copynumber and BAF data. GenoSet class extends
eSet by adding a "locData" slot for a RangedData object from the IRanges
package. This object contains feature genome location data and provides
for simple subsetting on genome location. CNSet and BAFSet extend GenoSet
and require assayData matrices for Copy Number (cn) or Log-R Ratio (lrr)
and B-Allele Frequency (baf) data. Implements and provides convenience
functions for processing of copy number and B-Allele Frequency data.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora