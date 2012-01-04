%global packname  TSgetSymbol
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.2
Release:          1%{?dist}
Summary:          Time Series Database Interface extension to connect with getSymbols

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI R-TSdbi R-tframe R-tframePlus R-quantmod 
Requires:         R-methods R-DBI R-TSdbi 

BuildRequires:    R-devel tex(latex) R-methods R-DBI R-TSdbi R-tframe R-tframePlus R-quantmod
BuildRequires:    R-methods R-DBI R-TSdbi 


%description
Provides methods for generics in the TSdbi package to retrieve data with
getSymbols, in particular from the Federal Reserve FRED database.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.2-1
- initial package for Fedora