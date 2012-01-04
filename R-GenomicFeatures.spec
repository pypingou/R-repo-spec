%global packname  GenomicFeatures
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.5
Release:          1%{?dist}
Summary:          Tools for making and manipulating transcript centric annotations

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-IRanges R-GenomicRanges R-AnnotationDbi 
Requires:         R-methods R-DBI R-RSQLite R-IRanges R-GenomicRanges R-Biostrings R-rtracklayer R-biomaRt R-RCurl R-utils R-Biobase 

BuildRequires:    R-devel tex(latex) R-IRanges R-GenomicRanges R-AnnotationDbi
BuildRequires:    R-methods R-DBI R-RSQLite R-IRanges R-GenomicRanges R-Biostrings R-rtracklayer R-biomaRt R-RCurl R-utils R-Biobase 


%description
A set of tools and methods for making and manipulating transcript centric
annotations. With these tools the user can easily download the genomic
locations of the transcripts, exons and cds of a given organism, from
either the UCSC Genome Browser or a BioMart database (more sources will be
supported in the future). This information is then stored in a local
database that keeps track of the relationship between transcripts, exons,
cds and genes. Flexible methods are provided for extracting the desired
features in a convenient format.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.5-1
- initial package for Fedora