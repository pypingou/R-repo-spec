%global packname  RNAinteractMAPK
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Mapping of Signalling Networks through Synthetic Genetic Interaction Analysis by RNAi

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-fields R-sparseLDA R-RNAinteract 

BuildRequires:    R-devel tex(latex) R-fields R-sparseLDA R-RNAinteract 

%description
This package includes all data used in the paper -Mapping of Signalling
Networks through Synthetic Genetic Interaction Analysis by RNAi- by Horn,
Sandmann, Fischer et al.., Nat. Methods, 2011. The package vignette shows
the R code to reproduce all figures in the paper.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora