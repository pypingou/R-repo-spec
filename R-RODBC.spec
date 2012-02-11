%global packname  RODBC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.4
Release:          1%{dist}
Summary:          ODBC Database Access

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 
Requires:         unixODBC
BuildRequires:    R-devel tex(latex) R-utils
BuildRequires:    unixODBC-devel

%description
An ODBC database interface

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
%doc %{rlibdir}/RODBC/DESCRIPTION
%doc %{rlibdir}/RODBC/html
%doc %{rlibdir}/RODBC/LICENCE
%{rlibdir}/RODBC/INDEX
%{rlibdir}/RODBC/tests.R
%{rlibdir}/RODBC/help
%{rlibdir}/RODBC/NAMESPACE
%{rlibdir}/RODBC/R
%{rlibdir}/RODBC/libs
%{rlibdir}/RODBC/Meta
%{rlibdir}/RODBC/po
%{rlibdir}/RODBC/doc

%changelog
* Sat Feb 11 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.4-1
- Update to version 1.3.4

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.3-1
- initial package for Fedora
