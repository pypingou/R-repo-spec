%global packname  nnNorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.18.0
Release:          1%{?dist}
Summary:          Spatial and intensity based normalization of cDNA microarray data based on robust neural nets

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-marray 

BuildRequires:    R-devel tex(latex) R-marray 

%description
This package allows to detect and correct for spatial and intensity biases
with two-channel microarray data. The normalization method implemented in
this package is based on robust neural networks fitting.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.18.0-1
- initial package for Fedora