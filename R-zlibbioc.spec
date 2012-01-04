%global packname  zlibbioc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          An R packaged zlib-1.2.5

Group:            Applications/Engineering 
License:          Artistic-2.0 + file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package uses the source code of zlib-1.2.5 to create libraries for
systems that do not have these available via other means (most Linux and
Mac users should have system-level access to zlib, and no direct need for
this package). See the vignette for instructions on use.

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
%doc %{rlibdir}/zlibbioc/html
%doc %{rlibdir}/zlibbioc/doc
%doc %{rlibdir}/zlibbioc/DESCRIPTION
%{rlibdir}/zlibbioc/Meta
%{rlibdir}/zlibbioc/NAMESPACE
%{rlibdir}/zlibbioc/libs
%{rlibdir}/zlibbioc/R
%{rlibdir}/zlibbioc/help
%{rlibdir}/zlibbioc/INDEX
%{rlibdir}/zlibbioc/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora