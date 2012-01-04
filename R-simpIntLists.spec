%global packname  simpIntLists
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.1
Release:          1%{?dist}
Summary:          The package contains BioGRID interactions for various organisms in a simple format

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package contains BioGRID interactions for arabidopsis(thale cress),
c.elegans, fruit fly, human, mouse, yeast( budding yeast ) and S.pombe
(fission yeast) . Entrez ids, official names and unique ids can be used to
find proteins. The format of interactions are lists. For each
gene/protein, there is an entry in the list with "name" containing name of
the gene/protein and "interactors" containing the list of genes/proteins
interacting with it.

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
%doc %{rlibdir}/simpIntLists/html
%doc %{rlibdir}/simpIntLists/DESCRIPTION
%doc %{rlibdir}/simpIntLists/doc
%{rlibdir}/simpIntLists/data
%{rlibdir}/simpIntLists/NAMESPACE
%{rlibdir}/simpIntLists/R
%{rlibdir}/simpIntLists/help
%{rlibdir}/simpIntLists/Meta
%{rlibdir}/simpIntLists/INDEX
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.1-1
- initial package for Fedora