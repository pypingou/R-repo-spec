%global packname  DBI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          R Database Interface

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
A database interface (DBI) definition for communication between R and
relational database management systems.  All classes in this package are
virtual and need to be extended by the various R/DBMS implementations.

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
%doc %{rlibdir}/DBI/html
%doc %{rlibdir}/DBI/doc
%doc %{rlibdir}/DBI/NEWS
%doc %{rlibdir}/DBI/DESCRIPTION
%{rlibdir}/DBI/Meta
%{rlibdir}/DBI/help
%{rlibdir}/DBI/TODO
%{rlibdir}/DBI/INDEX
%{rlibdir}/DBI/R
%{rlibdir}/DBI/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora