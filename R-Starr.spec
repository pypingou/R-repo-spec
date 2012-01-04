%global packname  Starr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Simple tiling array analysis of Affymetrix ChIP-chip data

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Ringo R-affy R-affxparser 

BuildRequires:    R-devel tex(latex) R-Ringo R-affy R-affxparser 

%description
Starr facilitates the analysis of ChIP-chip data, in particular that of
Affymetrix tiling arrays. The package provides functions for data import,
quality assessment, data visualization and exploration. Furthermore, it
includes high-level analysis features like association of ChIP signals
with annotated features, correlation analysis of ChIP signals and other
genomic data (e.g. gene expression), peak-finding with the CMARRT
algorithm and comparative display of multiple clusters of ChIP-profiles.
It uses the basic Bioconductor classes ExpressionSet and probeAnno for
maximum compatibility with other software on Bioconductor. All functions
from Starr can be used to investigate preprocessed data from the Ringo
package, and vice versa. An important novel tool is the the automated
generation of correct, up-to-date microarray probe annotation (bpmap)
files, which relies on an efficient mapping of short sequences (e.g. the
probe sequences on a microarray) to an arbitrary genome.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora