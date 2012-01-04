%global packname  maDB
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Microarray database and utility functions for microarray data analysis.

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-affy R-pgUtils R-limma R-methods 


BuildRequires:    R-devel tex(latex) R-Biobase R-affy R-pgUtils R-limma R-methods



%description
maDB allows to create a simple microarray database to store microarray
experiments and annotation data into it. Affymetrix GeneChip expression
values as well as values from two color microarrays can be stored into the
database. Whole experiments or subsets from a experiment (or also values
for a subset of genes in a subset of microarrays) can be fetched back to
R. Additionally maDB provides different utility functions for the
microarray data analysis like functions to draw MA plots or volcano plots
with the data points color coded according to the local point density or
functions that allow a replicate handling of miroarrays.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora