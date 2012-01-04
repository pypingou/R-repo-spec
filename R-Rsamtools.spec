%global packname  Rsamtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.2
Release:          1%{?dist}
Summary:          Binary alignment (BAM), variant call (BCF), or tabix file import

Group:            Applications/Engineering 
License:          Artistic-2.0 + file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-IRanges R-GenomicRanges R-Biostrings 
Requires:         R-methods R-utils R-IRanges R-GenomicRanges R-Biostrings R-zlibbioc R-rtracklayer R-bitops 

BuildRequires:    R-devel tex(latex) R-methods R-IRanges R-GenomicRanges R-Biostrings
BuildRequires:    R-methods R-utils R-IRanges R-GenomicRanges R-Biostrings R-zlibbioc R-rtracklayer R-bitops 


%description
This package provides an interface to the 'samtools', 'bcftools', and
'tabix' utilities (see 'LICENCE') for manipulating SAM (Sequence Alignment
/ Map), binary variant call (BCF) and compressed indexed tab-delimited
(tabix) files.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.2-1
- initial package for Fedora