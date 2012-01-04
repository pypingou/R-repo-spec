%global packname  TSpadi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.2
Release:          1%{?dist}
Summary:          Time Series Database Interface extensions for PADI Time Series Server

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI R-TSdbi R-tframe 
Requires:         R-methods R-DBI R-TSdbi 

BuildRequires:    R-devel tex(latex) R-methods R-DBI R-TSdbi R-tframe
BuildRequires:    R-methods R-DBI R-TSdbi 


%description
Provides methods for generics in the TSdbi package to connect through a
protocol for application database interface (PADI) to a time series
database (e.g. Fame).

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
%doc %{rlibdir}/TSpadi/doc
%doc %{rlibdir}/TSpadi/html
%doc %{rlibdir}/TSpadi/DESCRIPTION
%doc %{rlibdir}/TSpadi/NEWS
%{rlibdir}/TSpadi/exec
%{rlibdir}/TSpadi/Meta
%{rlibdir}/TSpadi/libs
%{rlibdir}/TSpadi/LICENSE
%{rlibdir}/TSpadi/NAMESPACE
%{rlibdir}/TSpadi/help
%{rlibdir}/TSpadi/R
%{rlibdir}/TSpadi/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.2-1
- initial package for Fedora