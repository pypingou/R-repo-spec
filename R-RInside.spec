%global packname  RInside
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          C++ classes to embed R in C++ applications

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp 


BuildRequires:    R-devel tex(latex) R-Rcpp



%description
C++ classes to embed R in C++ applications The RInside packages makes it
easier to have 'R inside' your C++ application by providing a few wrapper
classes. . As R itself is embedded into your application, a shared library
build of R is required. This works on Linux, OS X and even on Windows
provided you use the same tools used to build R itself.  (NB: Windows
versions curretly seg.fault and debugging help would be appreciated. An
older version worked fine, but there may have been some Rcpp changes which
caused this.) . Numerous examples are provided in the three subdirectories
the examples/ directory of the installed package: standard, mpi (for
parallel computing) and qt (showing how to embed RInside inside a Qt
application). . Doxygen-generated documentation of the C++ classes is
available at the RInside website as well.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- initial package for Fedora