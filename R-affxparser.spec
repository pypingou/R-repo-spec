%global packname  affxparser
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.1
Release:          1%{?dist}
Summary:          Affymetrix File Parsing SDK

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Package for parsing Affymetrix files (CDF, CEL, CHP, BPMAP, BAR).  It
provides methods for fast and memory efficient parsing of Affymetrix files
using the Affymetrix' Fusion SDK.  Both ASCII- and binary-based files are
supported.  Currently, there are methods for reading chip definition file
(CDF) and a cell intensity file (CEL).  These files can be read either in
full or in part.  For example, probe signals from a few probesets can be
extracted very quickly from a set of CEL files into a convenient list

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.1-1
- initial package for Fedora