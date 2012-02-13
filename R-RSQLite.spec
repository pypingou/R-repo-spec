%global packname  RSQLite
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11.1
Release:          1%{dist}
Summary:          SQLite interface for R

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI 

BuildRequires:    R-devel tex(latex) R-methods R-DBI 

%description
Database Interface R driver for SQLite.  This package embeds the SQLite
database engine in R and provides an interface compliant with the DBI
package.  The source for the SQLite engine (version 3.7.8) is included.

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
%doc %{rlibdir}/RSQLite/DESCRIPTION
%doc %{rlibdir}/RSQLite/NEWS
%doc %{rlibdir}/RSQLite/html
%{rlibdir}/RSQLite/README
%{rlibdir}/RSQLite/R
%{rlibdir}/RSQLite/help
%{rlibdir}/RSQLite/INDEX
%{rlibdir}/RSQLite/UnitTests
%{rlibdir}/RSQLite/rsqlitePerf.txt
%{rlibdir}/RSQLite/include
%{rlibdir}/RSQLite/HACKING
%{rlibdir}/RSQLite/libs
%{rlibdir}/RSQLite/TODO
%{rlibdir}/RSQLite/THANKS
%{rlibdir}/RSQLite/ONEWS
%{rlibdir}/RSQLite/INSTALL
%{rlibdir}/RSQLite/Meta
%{rlibdir}/RSQLite/NAMESPACE
%{rlibdir}/RSQLite/announce

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11.1-1
- Update to version 0.11.1

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10.0-1
- initial package for Fedora