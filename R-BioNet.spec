%global packname  BioNet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Routines for the functional analysis of biological networks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-graph R-RBGL 

BuildRequires:    R-devel tex(latex) R-Biobase R-graph R-RBGL 

%description
This package provides functions for the integrated analysis of
protein-protein interaction networks and the detection of functional
modules. Different datasets can be integrated into the network by
assigning p-values of statistical tests to the nodes of the network. E.g.
p-values obtained from the differential expression of the genes from an
Affymetrix array are assigned to the nodes of the network. By fitting a
beta-uniform mixture model and calculating scores from the p-values,
overall scores of network regions can be calculated and an integer linear
programming algorithm identifies the maximum scoring subnetwork.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora