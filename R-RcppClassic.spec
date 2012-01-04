%global packname  RcppClassic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Deprecated 'classic' Rcpp API

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp R-methods 


BuildRequires:    R-devel tex(latex) R-Rcpp R-methods



%description
The RcppClassic package provides a decrecated C++ library which
facilitates the integration of R and C++. New project should use the new
Rcpp API in the Rcpp package

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora