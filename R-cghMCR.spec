%global packname  cghMCR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Find chromosome regions showing common gains/losses

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DNAcopy R-CNTools R-limma 

BuildRequires:    R-devel tex(latex) R-methods R-DNAcopy R-CNTools R-limma 

%description
This package provides functions to identify genomic regions of interests
based on segmented copy number data from multiple samples.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora