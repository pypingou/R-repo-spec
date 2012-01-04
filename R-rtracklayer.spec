%global packname  rtracklayer
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.4
Release:          1%{?dist}
Summary:          R interface to genome browsers and their annotation tracks

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-RCurl 
Requires:         R-XML R-IRanges R-GenomicRanges R-Biostrings R-BSgenome R-zlibbioc 

BuildRequires:    R-devel tex(latex) R-methods R-RCurl
BuildRequires:    R-XML R-IRanges R-GenomicRanges R-Biostrings R-BSgenome R-zlibbioc 


%description
Extensible framework for interacting with multiple genome browsers
(currently UCSC built-in) and manipulating annotation tracks in various
formats (currently GFF, BED, bedGraph, BED15, WIG, and BigWig built-in).
The user may export/import tracks to/from the supported browsers, as well
as query and modify the browser state, such as the current viewport.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.4-1
- initial package for Fedora