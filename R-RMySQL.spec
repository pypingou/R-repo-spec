%global packname  RMySQL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          R interface to the MySQL database

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI R-utils 


BuildRequires:    R-devel tex(latex) R-methods R-DBI R-utils



%description
Database interface and MySQL driver for R. This version complies with the
database interface definition as implemented in the package DBI 0.2-2.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.0-1
- initial package for Fedora