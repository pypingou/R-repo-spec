%global packname  GGtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.0.0
Release:          1%{?dist}
Summary:          software and data for genetics of gene expression (c) 2006 VJ Carey

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-GGBase R-snpStats R-annotate R-IRanges R-rtracklayer R-org.Hs.eg.db R-GenomicRanges R-ff 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-GGBase R-snpStats R-annotate R-IRanges R-rtracklayer R-org.Hs.eg.db R-GenomicRanges R-ff 

%description
dealing with hapmap SNP reports, GWAS, etc.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.0-1
- initial package for Fedora