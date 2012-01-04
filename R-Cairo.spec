%global packname  Cairo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          R graphics device using cairo graphics library for creating high-quality bitmap (PNG, JPEG, TIFF), vector (PDF, SVG, PostScript) and display (X11 and Win32) output.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a Cairo graphics device that can be use to create
high-quality vector (PDF, PostScript and SVG) and bitmap output
(PNG,JPEG,TIFF), and high-quality rendering in displays (X11 and Win32).
Since it uses the same back-end for all output, copying across formats is
WYSIWYG. Files are created without the dependence on X11 or other external
programs. This device supports alpha channel (semi-transparent drawing)
and resulting images can contain transparent and semi-transparent regions.
It is ideal for use in server environemnts (file output) and as a
replacement for other devices that don't have Cairo's capabilities such as
alpha support or anti-aliasing. Backends are modular such that any subset
of backends is supported.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora