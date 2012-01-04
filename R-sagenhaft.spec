%global packname  sagenhaft
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Collection of functions for reading and comparing SAGE libraries

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-SparseM R-methods 

BuildRequires:    R-devel tex(latex) R-SparseM R-methods 

%description
This package implements several functions useful for analysis of gene
expression data by sequencing tags as done in SAGE (Serial Analysis of
Gene Expressen) data, i.e. extraction of a SAGE library from sequence
files, sequence error correction, library comparison. Sequencing error
correction is implementing using an Expectation Maximization Algorithm
based on a Mixture Model of tag counts.

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
%doc %{rlibdir}/sagenhaft/html
%doc %{rlibdir}/sagenhaft/DESCRIPTION
%doc %{rlibdir}/sagenhaft/doc
%{rlibdir}/sagenhaft/data
%{rlibdir}/sagenhaft/R
%{rlibdir}/sagenhaft/Meta
%{rlibdir}/sagenhaft/extdata
%{rlibdir}/sagenhaft/help
%{rlibdir}/sagenhaft/NAMESPACE
%{rlibdir}/sagenhaft/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora