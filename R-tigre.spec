%global packname  tigre
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Transcription factor Inference through Gaussian process Reconstruction of Expression

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-Biobase R-methods R-AnnotationDbi R-gplots R-graphics R-puma R-stats R-utils R-annotate R-DBI R-RSQLite 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-Biobase R-methods R-AnnotationDbi R-gplots R-graphics R-puma R-stats R-utils R-annotate R-DBI R-RSQLite 


%description
The tigre package implements our methodology of Gaussian process
differential equation models for analysis of gene expression time series
from single input motif networks. The package can be used for inferring
unobserved transcription factor (TF) protein concentrations from
expression measurements of known target genes, or for ranking candidate
targets of a TF.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora