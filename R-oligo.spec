%global packname  oligo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          Preprocessing tools for oligonucleotide arrays.

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-oligoClasses 
Requires:         R-affyio R-affxparser R-Biobase R-Biostrings R-DBI R-ff R-graphics R-methods R-preprocessCore R-splines R-stats R-utils R-zlibbioc 

BuildRequires:    R-devel tex(latex) R-oligoClasses
BuildRequires:    R-affyio R-affxparser R-Biobase R-Biostrings R-DBI R-ff R-graphics R-methods R-preprocessCore R-splines R-stats R-utils R-zlibbioc 


%description
A package to analyze oligonucleotide arrays (expression/SNP/tiling/exon)
at probe-level. It currently supports Affymetrix (CEL files) and NimbleGen
arrays (XYS files).

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora