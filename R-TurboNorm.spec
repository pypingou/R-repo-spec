%global packname  TurboNorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          A fast scatterplot smoother suitable for microarray normalization

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-convert R-limma R-marray 
Requires:         R-stats R-grDevices R-affy R-lattice 

BuildRequires:    R-devel tex(latex) R-convert R-limma R-marray
BuildRequires:    R-stats R-grDevices R-affy R-lattice 


%description
A fast scatterplot smoother based on B-splines with second-order
difference penalty. Functions for microarray normalization of
single-colour data i.e. Affymetrix/Illumina and two-colour data supplied
as marray MarrayRaw-objects or limma RGList-objects are available.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora