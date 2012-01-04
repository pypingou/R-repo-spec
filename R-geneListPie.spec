%global packname  geneListPie
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Profiling a gene list into GOslim or KEGG function pie

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
"geneListPie" package is for mapping a gene list to function categories
defined in GOSlim or Kegg. The results can be plotted as a pie chart to
provide a quick view of the genes distribution of the gene list among the
function categories. The gene list must contain a list of gene symbols.
The package contains a set of pre-processed gene sets obtained from Gene
Ontology and MSigDB including human, mouse, rat and yeast. To provide a
high level concise view, only GO slim and kegg are provided. The gene sets
are regulared updated. User can also use customized gene sets. User can
use the R Pie() or Pie3D() function for plotting the pie chart. Users can
also choose to output the gene function mapping results and use external
software such as Excel(R) for ploting.

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
%doc %{rlibdir}/geneListPie/DESCRIPTION
%doc %{rlibdir}/geneListPie/html
%{rlibdir}/geneListPie/R
%{rlibdir}/geneListPie/INDEX
%{rlibdir}/geneListPie/help
%{rlibdir}/geneListPie/data
%{rlibdir}/geneListPie/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora