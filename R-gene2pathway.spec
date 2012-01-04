%global packname  gene2pathway
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.0
Release:          1%{?dist}
Summary:          Prediction of KEGG pathway membership for individual genes based on InterPro domain signatures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-kernlab R-biomaRt R-KEGGSOAP R-RBGL R-AnnotationDbi R-org.Dm.eg.db R-keggorthology 

BuildRequires:    R-devel tex(latex) R-kernlab R-biomaRt R-KEGGSOAP R-RBGL R-AnnotationDbi R-org.Dm.eg.db R-keggorthology 

%description
The package takes a list of genes and predicts to which KEGG pathway each
gene maps to. This is done by looking at the InterPro domains of each
gene. Each prediction is assigned a confidence score. The package also
allows to predict connected component membership of genes within signaling
pathways. Separate models for each organism supported by KEGG can be

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.0-1
- initial package for Fedora