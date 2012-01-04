%global packname  rredis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.3
Release:          1%{?dist}
Summary:          Redis client for R

Group:            Applications/Engineering 
License:          Apache License 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The 'redis' package provides a simple R client for the Redis persistent
key-value database available from http://redis.io.

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
%doc %{rlibdir}/rredis/doc
%doc %{rlibdir}/rredis/DESCRIPTION
%doc %{rlibdir}/rredis/html
%doc %{rlibdir}/rredis/NEWS
%{rlibdir}/rredis/INDEX
%{rlibdir}/rredis/Meta
%{rlibdir}/rredis/NAMESPACE
%{rlibdir}/rredis/help
%{rlibdir}/rredis/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.3-1
- initial package for Fedora