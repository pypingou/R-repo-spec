%global packname  apTreeshape
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.4
Release:          1%{?dist}
Summary:          Analyses of Phylogenetic Treeshape

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-ape R-quantreg 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-ape R-quantreg 


%description
apTreeshape is mainly dedicated to simulation and analysis of phylogenetic
tree topologies using statistical indices. It is a companion library of
the 'ape' package. It provides additional functions for reading, plotting,
manipulating phylogenetic trees. It also offers convenient web-access to
public databases, and enables testing null models of macroevolution using
corrected test statistics.  Trees of class "phylo" (from 'ape' package)
can be converted easily.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.4-1
- initial package for Fedora