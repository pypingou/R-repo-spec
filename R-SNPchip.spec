%global packname  SNPchip
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.1
Release:          1%{?dist}
Summary:          Classes and Methods for high throughput SNP chip data

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods R-oligoClasses R-graphics 
Requires:         R-Biobase R-graphics R-grDevices R-methods R-oligoClasses R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods R-oligoClasses R-graphics
BuildRequires:    R-Biobase R-graphics R-grDevices R-methods R-oligoClasses R-stats R-utils 


%description
This package defines classes and functions for plotting copy number and
genotype in high throughput SNP platforms such as Affymetrix and Illumina.
 In particular, SNPchip is a useful add-on to the oligo package for
visualizing SNP-level estimates after pre-processing.

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
%doc %{rlibdir}/SNPchip/DESCRIPTION
%doc %{rlibdir}/SNPchip/doc
%doc %{rlibdir}/SNPchip/html
%doc %{rlibdir}/SNPchip/CITATION
%{rlibdir}/SNPchip/NAMESPACE
%{rlibdir}/SNPchip/hg18
%{rlibdir}/SNPchip/Meta
%{rlibdir}/SNPchip/R
%{rlibdir}/SNPchip/data
%{rlibdir}/SNPchip/INDEX
%{rlibdir}/SNPchip/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.1-1
- initial package for Fedora