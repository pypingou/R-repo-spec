%global packname  ODB
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Open Document Databases (.odb) management

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-DBI R-RJDBC R-XML 

BuildRequires:    R-devel tex(latex) R-methods R-DBI R-RJDBC R-XML 

%description
This package provides functions to create, connect, update and query HSQL
databases embedded in Open Document Databases (.odb) files, as OpenOffice
and LibreOffice do.

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
%doc %{rlibdir}/ODB/DESCRIPTION
%doc %{rlibdir}/ODB/html
%{rlibdir}/ODB/Meta
%{rlibdir}/ODB/tools
%{rlibdir}/ODB/INDEX
%{rlibdir}/ODB/R
%{rlibdir}/ODB/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora