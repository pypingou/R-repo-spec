%global packname  biganalytics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.14
Release:          1%{?dist}
Summary:          A library of utilities for big.matrix objects of package bigmemory.

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-utils R-bigmemory 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-utils R-bigmemory 

%description
This package extends the bigmemory package with various analytics.
Functions bigkmeans and binit may also be used with native R objects. For
tapply-like functions, the bigtabulate package may also be helpful. For
linear algebra support, see bigalgebra.  For mutex (locking) support for
advanced shared-memory usage, see synchronicity.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.14-1
- initial package for Fedora