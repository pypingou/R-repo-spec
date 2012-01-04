%global packname  RPostgreSQL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          R interface to the PostgreSQL database system

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI 


BuildRequires:    R-devel tex(latex) R-methods R-DBI



%description
Database interface and PostgreSQL driver for R This package provides a
Database Interface (DBI) compliant driver for R to access PostgreSQL
database systems. . In order to build and install this package from
source, PostgreSQL itself must be present your system to provide
PostgreSQL functionality via its libraries and header files. These files
are provided as postgresql-devel package under some Linux distributions. .
On Microsoft Windows system the attached libpq library source will be
used. . A wiki and issue tracking system for the package are available at
Google Code at https://code.google.com/p/rpostgresql/ .

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora