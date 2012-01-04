%global packname  hyperSpec
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.98.20110927
Release:          1%{?dist}
Summary:          Interface for hyperspectral data, i.e. spectra + meta info (spatial, time, concentration, ...)

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.98-20110927.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-lattice R-grid 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-lattice R-grid 

%description
This package is an interface to handle hyperspectral data sets in R.  I.e.
spatially or time-resolved spectra, or spectra with any other kind of
information associated with each of the spectra. The spectra can be data
as obtained in XRF, UV/VIS, Fluorescence, AES, NIR, IR, Raman, NMR, MS,
etc. More generally, any data that is recorded over a discretized
variable, e.g.  absorbance = f (wavelength), stored as a vector of
absorbance values for discrete wavelengths is suitable.

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
%doc %{rlibdir}/hyperSpec/NEWS
%doc %{rlibdir}/hyperSpec/html
%doc %{rlibdir}/hyperSpec/CITATION
%doc %{rlibdir}/hyperSpec/DESCRIPTION
%doc %{rlibdir}/hyperSpec/doc
%{rlibdir}/hyperSpec/help
%{rlibdir}/hyperSpec/NAMESPACE
%{rlibdir}/hyperSpec/data
%{rlibdir}/hyperSpec/Meta
%{rlibdir}/hyperSpec/R
%{rlibdir}/hyperSpec/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.98.20110927-1
- initial package for Fedora