%global packname  SNPlocs.Hsapiens.dbSNP.20101109
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.6
Release:          1%{?dist}
Summary:          SNP locations for Homo sapiens (dbSNP Build 132)

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-IRanges R-GenomicRanges 
Requires:         R-methods R-IRanges R-GenomicRanges 

BuildRequires:    R-devel tex(latex) R-IRanges R-GenomicRanges
BuildRequires:    R-methods R-IRanges R-GenomicRanges 


%description
SNP locations and alleles for Homo sapiens extracted from NCBI dbSNP Build
132. The source data files used for this package were created by NCBI on 9
November 2010 and contain SNPs mapped to reference genome GRCh37. WARNING:
Note that the GRCh37 genome is the same as the hg19 genome from UCSC
except for the mitochondrion chromosome. Therefore, the SNPs in this
package can be "injected" in BSgenome.Hsapiens.UCSC.hg19 but this
injection will exclude chrM (i.e. nothing will be injected in that

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.6-1
- initial package for Fedora