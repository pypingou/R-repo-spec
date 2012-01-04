%global packname  iSubpathwayMiner
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          The package can implement the graph-based reconstruction, analyses, and visualization of the KEGG pathways.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-RBGL R-igraph R-XML R-fdrtool R-utils 

BuildRequires:    R-devel tex(latex) R-graph R-RBGL R-igraph R-XML R-fdrtool R-utils 

%description
The package can implement the graph-based reconstruction, analyses, and
visualization of the KEGG pathways. (1) Our system provides many
strategies of converting pathways to graph models. Ten functions related
to conversion from pathways to graphs are developed. Furthermore, the
combinations of these functions can get many combined conversion
strategies of pathway graphs (> 20). (2) The iSubpathwayMiner can support
the annotation and identification of pathways based on gene sets, compound
sets, and even the combined sets of genes and compounds. The entire
pathway and subpathway identification methods are available for these
sets. (3) The system can also support topology-based pathway analysis of
these sets. (4) We develop KEGG layout style of pathway graphs in R to
simulate the layout of the pathway picture in KEGG website. In addition,
our system has also provided many types of automatic layout styles.
Pathway graphs can also be exported to the GML format supported by
Cytoscape. (5) The iSubpathwayMiner can provide the most up-to-date
pathway analysis results for users. Multiple species (about 139
Eukaryotes, 1141 Bacteria and 93 Archaea) and different gene identifiers
(KEGG compound, Entrez Gene IDs, gene official symbol, NCBI-gi IDs,
UniProt IDs, PDB IDs, etc.) can also be supported by the system.

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora