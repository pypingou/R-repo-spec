%global packname  rtiff
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          A tiff reader for R.

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-pixmap 


BuildRequires:    R-devel tex(latex) R-pixmap



%description
This package will read and write TIFF format images and return them as a
pixmap object. Because the resulting object can be very large for even
modestly sized TIFF images, images can be reduced as they are read for
improved performance.  This package is a wrapper around libtiff
(www.libtiff.org), on which it depends (i.e. the libtiff shared library
must be on your PATH for the binary to work, and tiffio.h must be on your
system to build the package from source). By using libtiff's highlevel
TIFFReadRGBAImage function, this package inherently support a wide range
of image formats and compression schemes. This package also provides an
implementation of the Ridler Autothresholding algorithm for easy
generation of binary masks.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora