%global packname  mzR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          parser for netCDF, mzXML, mzData and mzML files (mass spectrometry data)

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp R-methods 
Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Rcpp R-methods
BuildRequires:    R-Biobase 


%description
mzR provides a unified API to the common file formats and parsers
available for mass spectrometry data. It comes with a wrapper for the ISB
random access parser for mass spectrometry mzXML, mzData and mzML files.
The package contains the original code written by the ISB, and a subset of
the proteowizard library for mzML. The netCDF reading code has previously
been used in XCMS.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora