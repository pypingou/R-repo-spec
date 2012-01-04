%global packname  genefu
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Relevant Functions for Gene Expression Analysis, Especially in Breast Cancer.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survcomp R-mclust 
Requires:         R-amap 

BuildRequires:    R-devel tex(latex) R-survcomp R-mclust
BuildRequires:    R-amap 


%description
This package contains functions implementing various tasks usually
required by gene expression analysis, especially in breast cancer studies:
gene mapping between different microarray platforms, identification of
molecular subtypes, implementation of published gene signatures, gene
selection, survival analysis, ...

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
%doc %{rlibdir}/genefu/html
%doc %{rlibdir}/genefu/DESCRIPTION
%doc %{rlibdir}/genefu/doc
%{rlibdir}/genefu/extdata
%{rlibdir}/genefu/INDEX
%{rlibdir}/genefu/data
%{rlibdir}/genefu/R
%{rlibdir}/genefu/NAMESPACE
%{rlibdir}/genefu/Meta
%{rlibdir}/genefu/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora