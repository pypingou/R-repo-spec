%global packname  ArrayTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          geneChip Analysis Package

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-Biobase R-methods 
Requires:         R-affy R-Biobase R-graphics R-grDevices R-limma R-methods R-stats R-utils R-xtable 

BuildRequires:    R-devel tex(latex) R-affy R-Biobase R-methods
BuildRequires:    R-affy R-Biobase R-graphics R-grDevices R-limma R-methods R-stats R-utils R-xtable 


%description
This package is designed to provide solutions for quality assessment and
to detect differentially expressed genes for the Affymetrix GeneChips,
including both 3' -arrays and gene 1.0-ST arrays. The package generates
comprehensive analysis reports in HTML format. Hyperlinks on the report
page will lead to a series of QC plots, processed data, and differentially
expressed gene lists. Differentially expressed genes are reported in
tabular format with annotations hyperlinked to online biological

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora