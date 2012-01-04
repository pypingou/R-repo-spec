%global packname  TShistQuote
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.1
Release:          1%{?dist}
Summary:          Time Series Database Interface extensions for get.hist.quote

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI R-TSdbi R-tseries R-tframe R-tframePlus R-zoo 
Requires:         R-methods R-DBI R-TSdbi 

BuildRequires:    R-devel tex(latex) R-methods R-DBI R-TSdbi R-tseries R-tframe R-tframePlus R-zoo
BuildRequires:    R-methods R-DBI R-TSdbi 


%description
Provides methods for generics in the TSdbi package to retrieve data from
historical quote URLs.

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
%doc %{rlibdir}/TShistQuote/DESCRIPTION
%doc %{rlibdir}/TShistQuote/NEWS
%doc %{rlibdir}/TShistQuote/doc
%doc %{rlibdir}/TShistQuote/html
%{rlibdir}/TShistQuote/INDEX
%{rlibdir}/TShistQuote/help
%{rlibdir}/TShistQuote/Meta
%{rlibdir}/TShistQuote/LICENSE
%{rlibdir}/TShistQuote/R
%{rlibdir}/TShistQuote/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.1-1
- initial package for Fedora