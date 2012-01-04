%global packname  RH2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2.7
Release:          1%{?dist}
Summary:          DBI/RJDBC interface to h2 Database

Group:            Applications/Engineering 
License:          Mozilla Public License 1.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-chron R-methods R-RJDBC 

BuildRequires:    R-devel tex(latex) R-chron R-methods R-RJDBC 

%description
DBI/RJDBC interface to h2 database. h2 version 1.3.158 is included.

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
%doc %{rlibdir}/RH2/html
%doc %{rlibdir}/RH2/NEWS
%doc %{rlibdir}/RH2/DESCRIPTION
%{rlibdir}/RH2/java
%{rlibdir}/RH2/R
%{rlibdir}/RH2/INDEX
%{rlibdir}/RH2/THANKS
%{rlibdir}/RH2/INSTALL
%{rlibdir}/RH2/Meta
%{rlibdir}/RH2/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2.7-1
- initial package for Fedora