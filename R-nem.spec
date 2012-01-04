%global packname  nem
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.18.0
Release:          1%{?dist}
Summary:          Nested Effects Models to reconstruct phenotypic hierarchies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-e1071 R-graph R-Rgraphviz R-plotrix R-limma R-time R-cluster R-statmod 
Requires:         R-boot R-e1071 R-graph R-graphics R-grDevices R-methods R-RBGL R-RColorBrewer R-Rgraphviz R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-e1071 R-graph R-Rgraphviz R-plotrix R-limma R-time R-cluster R-statmod
BuildRequires:    R-boot R-e1071 R-graph R-graphics R-grDevices R-methods R-RBGL R-RColorBrewer R-Rgraphviz R-stats R-utils 


%description
The package 'nem' allows to reconstruct features of pathways from the
nested structure of perturbation effects. It takes as input (1.) a set of
pathway components, which were perturbed, and (2.) high-dimensional
phenotypic readout of these perturbations (e.g. gene expression or
morphological profiles). The output is a directed graph representing the
phenotypic hierarchy.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.18.0-1
- initial package for Fedora