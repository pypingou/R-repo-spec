%global packname  ape
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.8
Release:          1%{?dist}
Summary:          Analyses of Phylogenetics and Evolution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-gee R-nlme R-lattice 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-gee R-nlme R-lattice 


%description
ape provides functions for reading, writing, plotting, and manipulating
phylogenetic trees, analyses of comparative data in a phylogenetic
framework, analyses of diversification and macroevolution, computing
distances from allelic and nucleotide data, reading nucleotide sequences,
and several tools such as Mantel's test, computation of minimum spanning
tree, generalized skyline plots, estimation of absolute evolutionary rates
and clock-like trees using mean path lengths, non-parametric rate
smoothing and penalized likelihood. Phylogeny estimation can be done with
the NJ, BIONJ, ME, MVR, SDM, and triangle methods, and several methods
handling incomplete distance matrices (NJ*, BIONJ*, MVR*, and the
corresponding triangle method).

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
%doc %{rlibdir}/ape/doc
%doc %{rlibdir}/ape/DESCRIPTION
%doc %{rlibdir}/ape/CITATION
%doc %{rlibdir}/ape/html
%doc %{rlibdir}/ape/LICENCE
%doc %{rlibdir}/ape/NEWS
%{rlibdir}/ape/NAMESPACE
%{rlibdir}/ape/Meta
%{rlibdir}/ape/libs
%{rlibdir}/ape/help
%{rlibdir}/ape/R
RPM build errors:
%{rlibdir}/ape/data
%{rlibdir}/ape/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.8-1
- initial package for Fedora