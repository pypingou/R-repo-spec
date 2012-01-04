%global packname  phybase
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Basic functions for phylogenetic analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-ape 


BuildRequires:    R-devel tex(latex) R-Matrix R-ape



%description
This package provides functions to read, write, manipulate, estimate, and
summarize phylogenetic trees including species trees which contain not
only the topology and branch lengths but also population sizes. The
input/output functions can read tree files in which trees are presented in
parenthetic format. The trees are read in as a string and then transformed
to a matrix which describes the relationship of nodes and branch lengths.
The nodes matrix provides an easy access for developers to further
manipulate the tree, while the tree string provides interface with other
phylogenetic R packages such as "ape". The input/output functions can also
be used to change the format of tree files between NEXUS and PHYLIP. Some
basic functions have already been established in the package for
manipulating trees such as deleting and swapping nodes, rooting and
unrooting trees, changing the root of the tree. The package also includes
functions such as "consensus", "coaltime, "popsize", "treedist" for
summarizing phylogenetic trees, calculating the coalescence time,
population size, and tree distance. The function maxtree is built in the
package to esimtate the species tree from multiple gene trees.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora