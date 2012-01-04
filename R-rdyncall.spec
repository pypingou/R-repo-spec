%global packname  rdyncall
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.3
Release:          1%{?dist}
Summary:          Improved Foreign Function Interface (FFI) and Dynamic Bindings to C Libraries (e.g. OpenGL)

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package provides a cross-platform framework for dynamic binding of C
libraries using a flexible Foreign Function Interface (FFI). The FFI
supports almost all fundamental C types, multiple calling conventions,
symbolic access to foreign C struct/union data types and wrapping of R
functions as C callback function pointers. Dynamic bindings to shared C
libraries are data-driven by cross-platform binding specification using a
compact plain text format ; an initial repository of bindings to a couple
of common C libraries (OpenGL, SDL, Expat, glew, CUDA, OpenCL, ODE, R)
comes with the package. The package includes a variety of technology demos
and OS-specific notes for installation of shared libraries.

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
%doc %{rlibdir}/rdyncall/doc
%doc %{rlibdir}/rdyncall/DESCRIPTION
%doc %{rlibdir}/rdyncall/html
%{rlibdir}/rdyncall/Meta
%{rlibdir}/rdyncall/dynports
%{rlibdir}/rdyncall/demo-files
%{rlibdir}/rdyncall/demo
%{rlibdir}/rdyncall/libs
%{rlibdir}/rdyncall/R
%{rlibdir}/rdyncall/INDEX
%{rlibdir}/rdyncall/LICENSE
%{rlibdir}/rdyncall/NAMESPACE
%{rlibdir}/rdyncall/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.3-1
- initial package for Fedora