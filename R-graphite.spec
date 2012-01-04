%global packname  graphite
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          GRAPH Interaction from pathway Topological Environment

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph 
Requires:         R-AnnotationDbi R-graph R-graphics R-methods R-org.Hs.eg.db R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-graph
BuildRequires:    R-AnnotationDbi R-graph R-graphics R-methods R-org.Hs.eg.db R-stats R-utils 


%description
Graph objects from pathway topology derived from NCI, KEGG, Biocarta and
Reactome databases.

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