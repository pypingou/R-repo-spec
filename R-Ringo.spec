%global packname  Ringo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          R Investigation of ChIP-chip Oligoarrays

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-RColorBrewer R-limma R-Matrix R-grid 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-RColorBrewer R-limma R-Matrix R-grid 

%description
The package Ringo facilitates the primary analysis of ChIP-chip data. The
main functionalities of the package are data read-in, quality assessment,
data visualisation and identification of genomic regions showing
enrichment in ChIP-chip. The package has functions to deal with two-color
oligonucleotide microarrays from NimbleGen used in ChIP-chip projects, but
also contains more general functions for ChIP-chip data analysis, given
that the data is supplied as RGList (raw)  or ExpressionSet (pre-
processed). The package employs functions from various other packages of
the Bioconductor project and provides additional ChIP-chip-specific and
NimbleGen-specific functionalities.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora