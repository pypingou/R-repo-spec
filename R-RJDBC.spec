%global packname  RJDBC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Provides access to databases through the JDBC interface

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-DBI R-rJava 

BuildRequires:    R-devel tex(latex) R-methods R-DBI R-rJava 

%description
RJDBC is an implementation of R's DBI interface using JDBC as a back-end.
This allows R to connect to any DBMS that has a JDBC driver.

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
%doc %{rlibdir}/RJDBC/html
%doc %{rlibdir}/RJDBC/NEWS
%doc %{rlibdir}/RJDBC/DESCRIPTION
%{rlibdir}/RJDBC/R
%{rlibdir}/RJDBC/INDEX
%{rlibdir}/RJDBC/Meta
%{rlibdir}/RJDBC/help
%{rlibdir}/RJDBC/java

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora