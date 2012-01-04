%global packname  RpgSQL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          DBI/RJDBC interface to PostgreSQL Database

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-RJDBC 

BuildRequires:    R-devel tex(latex) R-methods R-RJDBC 

%description
DBI interface to PostgreSQL database via RJDBC.

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
%doc %{rlibdir}/RpgSQL/DESCRIPTION
%doc %{rlibdir}/RpgSQL/html
%doc %{rlibdir}/RpgSQL/NEWS
%{rlibdir}/RpgSQL/help
%{rlibdir}/RpgSQL/R
%{rlibdir}/RpgSQL/INDEX
%{rlibdir}/RpgSQL/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora