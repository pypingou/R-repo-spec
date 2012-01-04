%global packname  FITSio
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          FITS (Flexible Image Transport System) utilities

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Utilities to read and write files in the FITS (Flexible Image Transport
System) format, a standard format in astronomy. Present low-level routines
allow: * Reading and parsing FITS headers * Reading FITS images
(multi-dimensional arrays) * Reading FITS binary tables * Writing FITS
images (multi-dimensional arrays) Higher-level functions allow: * Reading
files composed of one or more headers and a single (perhaps
multidimensional) image or single bintable * Reading bintables into data
frames * Generating vectors for image array axes * Scaling and writing
images as 16-bit integers Known incompletenesses are reading FITS ASCII
table and random group extensions, as well as bit, complex, and array
descriptor data types in binary tables.

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
%doc %{rlibdir}/FITSio/DESCRIPTION
%doc %{rlibdir}/FITSio/html
%{rlibdir}/FITSio/help
%{rlibdir}/FITSio/Meta
%{rlibdir}/FITSio/R
%{rlibdir}/FITSio/fitsExamples
%{rlibdir}/FITSio/NAMESPACE
%{rlibdir}/FITSio/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora