%global packname  tilingArray
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Transcript mapping with high-density oligonucleotide tiling arrays

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods R-pixmap 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods R-pixmap 

%description
The package provides functionality that can be useful for the analysis of
high-density tiling microarray data (such as from Affymetrix genechips)
for measuring transcript abundance and architecture. The main
functionalities of the package are: 1. the class 'segmentation' for
representing partitionings of a linear series of data; 2. the function
'segment' for fitting piecewise constant models using a dynamic
programming algorithm that is both fast and exact; 3. the function
'confint' for calculating confidence intervals using the strucchange
package; 4. the function 'plotAlongChrom' for generating pretty plots; 5.
the function 'normalizeByReference' for probe-sequence dependent response
adjustment from a (set of) reference hybridizations.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora