%global packname  MEDIPS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          MeDIP-Seq data analysis

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-BSgenome 
Requires:         R-Biostrings R-BSgenome R-graphics R-gtools R-IRanges R-methods R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-BSgenome
BuildRequires:    R-Biostrings R-BSgenome R-graphics R-gtools R-IRanges R-methods R-stats R-utils 


%description
MEDIPS was developed for analyzing data derived from methylated DNA
immunoprecipitation (MeDIP) experiments followed by sequencing
(MeDIP-Seq). Nevertheless, functionalities like the quality controls may
be applied to other types of sequencing data (e.g. ChIP-Seq). MEDIPS
adresses several aspects in the context of MeDIP-Seq data analysis.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora