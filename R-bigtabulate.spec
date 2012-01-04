%global packname  bigtabulate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.13
Release:          1%{?dist}
Summary:          table-, tapply-, and split-like functionality for matrix and big.matrix objects.

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-bigmemory 

BuildRequires:    R-devel tex(latex) R-methods R-bigmemory 

%description
This package extends the bigmemory package with table- and split-like
support for big.matrix objects.  The functions may also be used with
regular R matrices for improving speed and memory-efficiency.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.13-1
- initial package for Fedora