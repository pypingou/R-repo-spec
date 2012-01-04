%global packname  int64
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          64 bit integer types

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
64 bit integer types

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
%doc %{rlibdir}/int64/doc
%doc %{rlibdir}/int64/DESCRIPTION
%doc %{rlibdir}/int64/html
%doc %{rlibdir}/int64/NEWS
%{rlibdir}/int64/include
%{rlibdir}/int64/unitTests
%{rlibdir}/int64/libs
%{rlibdir}/int64/Meta
%{rlibdir}/int64/NAMESPACE
%{rlibdir}/int64/R
%{rlibdir}/int64/INDEX
%{rlibdir}/int64/help

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora