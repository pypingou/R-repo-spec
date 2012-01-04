%global packname  biOps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1.1
Release:          1%{?dist}
Summary:          Image processing and analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package includes several methods for image processing and analysis.
It provides geometric, arithmetic, logic, morphologic (supported on one
channel images only), look-up tables, edge detection (including Roberts,
Sobel, Kirsch, Marr-Hildreth and Canny, among others) and convolution
masks operations (predefined commons masks already defined and user
defined applications). Isodata and k-means classification methods are also
provided (standard, kd-tree and brute force methods implemented). Fast
Fourier Transform methods and filters also available if fftw3 installed.
Supports jpeg and tiff images so far (more image support in future
versions). libtiff and libjpeg libraries installed required.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1.1-1
- initial package for Fedora