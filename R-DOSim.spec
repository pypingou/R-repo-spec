%global packname  DOSim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Disease Analysis toolkit for gene set; Computation of similarities between DO terms and disease similarity between gene products; Module detection among the gene set and multilayer annotation for each module.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GOSim R-SubpathwayMiner R-dynamicTreeCut R-moduleColor R-RBGL R-graph R-Rgraphviz 

BuildRequires:    R-devel tex(latex) R-GOSim R-SubpathwayMiner R-dynamicTreeCut R-moduleColor R-RBGL R-graph R-Rgraphviz 

%description
This package implements multiple similarity measures for DO terms and gene
products. It is aiming at disease analyis for gene sets. Modules of a gene
set could be detected and further multilayer annoated on DO, GO and KEGG.
We also provides users to conduct DO enrichment analysis and basic
information fetching for DO.DOSim: An R package for similarity between
diseases based on Disease

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora