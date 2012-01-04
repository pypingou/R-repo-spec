%global packname  GOFunction
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          GO-function: deriving biologcially relevant functions from statistically significant functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-graph R-Rgraphviz R-GO.db R-AnnotationDbi R-SparseM 
Requires:         R-methods R-Biobase R-graph R-Rgraphviz R-GO.db R-AnnotationDbi R-SparseM 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-graph R-Rgraphviz R-GO.db R-AnnotationDbi R-SparseM
BuildRequires:    R-methods R-Biobase R-graph R-Rgraphviz R-GO.db R-AnnotationDbi R-SparseM 


%description
The GO-function package provides a tool to address the redundancy that
result from the GO structure or multiple annotation genes and derive
biologically relevant functions from the statistically significant
functions based on some intuitive assumption and statistical testing.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora