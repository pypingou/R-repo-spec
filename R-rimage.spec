%global packname  rimage
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.8.2
Release:          1%{?dist}
Summary:          Image Processing Module for R

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-8.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions for image processing, including sobel
filter, rank filters, fft, histogram equalization, and reading JPEG file.
This package requires fftw-2 <http://www.fftw.org/> and libjpeg
<http://www.ijg.org>. This version doesn't require pixmap package, which
the older version of rimage (private only) required. This package can be
used on Unixes / MacOS X / Windows.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.8.2-1
- initial package for Fedora