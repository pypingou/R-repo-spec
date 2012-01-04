%global packname  TSdbi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.2
Release:          1%{?dist}
Summary:          Time Series Database Interface

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-tframe 
Requires:         R-methods R-DBI 

BuildRequires:    R-devel tex(latex) R-methods R-tframe
BuildRequires:    R-methods R-DBI 


%description
TSdbi provides a common interface to time series databases. The objective
is to define a standard interface so users can retrieve time series data
from various sources with a simple, common, set of commands, and so
programs can be written to be portable with respect to the data source.
The SQL implementations also provide a database table design, so users
needing to set up a time series database have a reasonably complete way to
do this easily. The interface provides for a variety of options with
respect to the representation of time series in R. There is also a (not
yet well tested) mechanism to handle multilingual data documentation.

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
%doc %{rlibdir}/TSdbi/doc
%doc %{rlibdir}/TSdbi/html
%doc %{rlibdir}/TSdbi/DESCRIPTION
%doc %{rlibdir}/TSdbi/NEWS
%{rlibdir}/TSdbi/TSsql
%{rlibdir}/TSdbi/LICENSE
%{rlibdir}/TSdbi/help
%{rlibdir}/TSdbi/INDEX
%{rlibdir}/TSdbi/Meta
%{rlibdir}/TSdbi/NAMESPACE
%{rlibdir}/TSdbi/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.2-1
- initial package for Fedora