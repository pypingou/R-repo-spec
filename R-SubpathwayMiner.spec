%global packname  SubpathwayMiner
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          A software package for annotation and identification of the KEGG pathways.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RBGL R-fdrtool R-utils 


BuildRequires:    R-devel tex(latex) R-RBGL R-fdrtool R-utils



%description
SubpathwayMiner is an R-based software for flexible pathway
identification. (1) SubpathwayMiner can provide users with sub-pathway
annotation and identification of metabolic pathways based on enzyme
commission (EC) numbers. (2) SubpathwayMiner can provide users with
sub-pathway annotation and identification based on KEGG Orthology (KO)
identifiers. (3) SubpathwayMiner can provide annotation and identification
of entire pathways. (4) SubpathwayMiner can support most of organisms in
the KEGG GENE database. (5) Data can be automatically updated on demand by
the user. (6) SubpathwayMiner can provide identification of disease
related sub-pathways.(new!) The version 3.1 use a new approach to store
organism-related data (e.g., gene-enzyme relation data), which make the
running time of the function updateOrgAndIdType reduce significantly
compared with the old version. Therefore, the environment variables of
organisms will be provided no longer for reducing size of the software
package. When using this tool, please cite: Li, C., Li, X., Miao, Y.,
Wang, Q., Jiang, W., Xu, C., Li, J., Han, J., Zhang, F., Gong, B. et al.
(2009) SubpathwayMiner: a software package for flexible identification of
pathways. Nucleic Acids Res, 37, e131. Full text:

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
%doc %{rlibdir}/SubpathwayMiner/DESCRIPTION
%doc %{rlibdir}/SubpathwayMiner/doc
%doc %{rlibdir}/SubpathwayMiner/html
%{rlibdir}/SubpathwayMiner/localdata
%{rlibdir}/SubpathwayMiner/R
%{rlibdir}/SubpathwayMiner/data
%{rlibdir}/SubpathwayMiner/NAMESPACE
%{rlibdir}/SubpathwayMiner/INDEX
%{rlibdir}/SubpathwayMiner/help
%{rlibdir}/SubpathwayMiner/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1-1
- initial package for Fedora