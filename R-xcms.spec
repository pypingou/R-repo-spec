%global packname  xcms
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.1
Release:          1%{?dist}
Summary:          LC/MS and GC/MS Data Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Framework for processing and visualization of chromatographically
separated and single-spectra mass spectral data. Imports from AIA/ANDI
NetCDF, mzXML, mzData and mzML files. Preprocesses data for
high-throughput, untargeted analyte profiling.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.1-1
- initial package for Fedora