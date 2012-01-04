%global packname  NCBI2R
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.4
Release:          1%{?dist}
Summary:          NCBI2R-An R package to navigate and annotate genes and SNPs

Group:            Applications/Engineering 
License:          GPL (> 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
NCBI2R is a R package that annotates lists of SNPs and/or genes, with
current information from NCBI, including LD information. Functions are
provided that with one command will provide annotation of the results from
genome wide association studies to provide a broader context of their
meaning. Other functions enable comparisons between a user's GWA results,
and candidate snp/gene lists that are created from keywords, such as
specific diseases, phenotypes or gene ontology terms. Commands are simple
to follow and designed to work with R objects to integrate into existing
workflows. The output produces text fields and weblinks to more
information for items such as: gene descriptions, nucleotide positions,
OMIM, pathways, phenotypes, and lists of interacting and neighboring
genes. Annotation can then be used in R for further analysis, or the
objects can be customized for use in spreadsheet programs or web browsers.
The NCBI2R package was designed to allow those performing genome analysis
to produce output that could easily be understood by a person not familiar
with R. Please see the new website at http://NCBI2R.wordpress.com for more
information. The internet is required for almost all of these functions.
Type PrintNCBI2RInfo() for information.

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
%doc %{rlibdir}/NCBI2R/html
%doc %{rlibdir}/NCBI2R/DESCRIPTION
%{rlibdir}/NCBI2R/Meta
%{rlibdir}/NCBI2R/INDEX
%{rlibdir}/NCBI2R/help
%{rlibdir}/NCBI2R/NAMESPACE
%{rlibdir}/NCBI2R/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.4-1
- initial package for Fedora