%global packname  MassArray
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Analytical Tools for MassArray Data

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package is designed for the import, quality control, analysis, and
visualization of methylation data generated using Sequenom's MassArray
platform.  The tools herein contain a highly detailed amplicon prediction
for optimal assay design.  Also included are quality control measures of
data, such as primer dimer and bisulfite conversion efficiency estimation.
 Methylation data are calculated using the same algorithms contained in
the EpiTyper software package.  Additionally, automatic SNP-detection can
be used to flag potentially confounded data from specific CG sites. 
Visualization includes barplots of methylation data as well as UCSC Genome
Browser-compatible BED tracks.  Multiple assays can be positionally
combined for integrated analysis.

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
%doc %{rlibdir}/MassArray/doc
%doc %{rlibdir}/MassArray/DESCRIPTION
%doc %{rlibdir}/MassArray/html
%{rlibdir}/MassArray/R
%{rlibdir}/MassArray/data
%{rlibdir}/MassArray/INDEX
%{rlibdir}/MassArray/NAMESPACE
%{rlibdir}/MassArray/help
%{rlibdir}/MassArray/Meta
%{rlibdir}/MassArray/extdata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora