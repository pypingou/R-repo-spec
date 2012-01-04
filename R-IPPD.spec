%global packname  IPPD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Isotopic peak pattern deconvolution for Protein Mass Spectrometry by template matching

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-Matrix 

BuildRequires:    R-devel tex(latex) R-MASS R-Matrix 

%description
The package provides functionality to extract isotopic peak patterns from
raw mass spectra. This is done by fitting a large set of template basis
functions to the raw spectrum using either nonnegative least squares or
least absolute deviation fittting. The package offers a flexible function
which tries to estimate model parameters in a way tailored to the peak
shapes in the data.

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
%doc %{rlibdir}/IPPD/doc
%doc %{rlibdir}/IPPD/DESCRIPTION
%doc %{rlibdir}/IPPD/news
%doc %{rlibdir}/IPPD/html
%{rlibdir}/IPPD/help
%{rlibdir}/IPPD/INDEX
%{rlibdir}/IPPD/Meta
%{rlibdir}/IPPD/NAMESPACE
%{rlibdir}/IPPD/libs
%{rlibdir}/IPPD/R
%{rlibdir}/IPPD/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora