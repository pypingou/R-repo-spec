%global packname  EatonEtAlChIPseq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          ChIP-seq data of ORC-binding sites in Yeast excerpted from Eaton et al. 2010

Group:            Applications/Engineering 
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-GenomicRanges R-ShortRead R-rtracklayer 

BuildRequires:    R-devel tex(latex) R-GenomicRanges R-ShortRead R-rtracklayer 

%description
ChIP-seq analysis subset from "Conserved nucleosome positioning defines
replication origins" (PMID 20351051)

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora