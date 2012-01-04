%global packname  oneChannelGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.3
Release:          1%{?dist}
Summary:          A graphical interface designed to facilitate analysis of microarrays and miRNA/RNA-seq data on laptops.

Group:            Applications/Engineering 
License:          The Artistic License, Version 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-limma R-affylmGUI R-tkWidgets R-GOstats R-AnnotationDbi R-preprocessCore R-IRanges R-baySeq R-Rsamtools R-R.utils 

BuildRequires:    R-devel tex(latex) R-Biobase R-limma R-affylmGUI R-tkWidgets R-GOstats R-AnnotationDbi R-preprocessCore R-IRanges R-baySeq R-Rsamtools R-R.utils 

%description
This package was developed to simplify the use of Bioconductor tools for
beginners having limited or no experience in writing R code. This library
provides a graphical interface for microarray gene and exon level analysis
as well as basic secondary analysis of NGS data for ncRNA quantification.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.3-1
- initial package for Fedora