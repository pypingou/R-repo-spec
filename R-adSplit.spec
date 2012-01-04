%global packname  adSplit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Annotation-Driven Clustering

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-AnnotationDbi R-Biobase R-cluster R-GO.db R-graphics R-grDevices R-KEGG.db R-methods R-multtest R-stats 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-AnnotationDbi R-Biobase R-cluster R-GO.db R-graphics R-grDevices R-KEGG.db R-methods R-multtest R-stats 


%description
This package implements clustering of microarray gene expression profiles
according to functional annotations. For each term genes are annotated to,
splits into two subclasses are computed and a significance of the
supporting gene set is determined.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora