%global packname  cairoDevice
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.19
Release:          1%{?dist}
Summary:          Cairo-based cross-platform antialiased graphics device driver.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Cairo/GTK graphics device driver with output to screen, file (png, svg,
pdf, and ps) or memory (arbitrary GdkDrawable or Cairo context). The
screen device may be embedded into RGtk2 interfaces. Supports all
interactive features of other graphics devices, including

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.19-1
- initial package for Fedora