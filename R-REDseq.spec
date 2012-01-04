%global packname  REDseq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Analysis of high-throughput sequencing data processed by restriction enzyme digestion

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-BSgenome.Celegans.UCSC.ce2 R-multtest R-Biostrings R-BSgenome R-ChIPpeakAnno 

BuildRequires:    R-devel tex(latex) R-BSgenome.Celegans.UCSC.ce2 R-multtest R-Biostrings R-BSgenome R-ChIPpeakAnno 

%description
The package includes functions to build restriction enzyme cut site (RECS)
map, distribute mapped sequences on the map with five different
approaches, find enriched/depleted RECSs for a sample, and identify
differentially enriched/depleted RECSs between samples.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora