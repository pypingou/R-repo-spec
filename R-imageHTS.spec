%global packname  imageHTS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Analysis of high-throughput microscopy-based screens

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-EBImage R-cellHTS2 

BuildRequires:    R-devel tex(latex) R-EBImage R-cellHTS2 

%description
imageHTS is an R package dedicated to the analysis of high-throughput
microscopy-based screens. The package provides a modular and extensible
framework to segment cells, extract quantitative cell features, predict
cell types and browse screen data through web interfaces. Designed to
operate in distributed environments, imageHTS provides a standardized
access to remote screen data, facilitating the dissemination of
high-throughput microscopy-based screens.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora