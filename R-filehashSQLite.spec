%global packname  filehashSQLite
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Simple key-value database using SQLite

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-filehash R-DBI R-RSQLite 

BuildRequires:    R-devel tex(latex) R-methods R-filehash R-DBI R-RSQLite 

%description
Simple key-value database using SQLite as the backend

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
%doc %{rlibdir}/filehashSQLite/COPYING
%doc %{rlibdir}/filehashSQLite/html
%doc %{rlibdir}/filehashSQLite/DESCRIPTION
%{rlibdir}/filehashSQLite/Meta
%{rlibdir}/filehashSQLite/INDEX
%{rlibdir}/filehashSQLite/help
%{rlibdir}/filehashSQLite/NAMESPACE
%{rlibdir}/filehashSQLite/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora