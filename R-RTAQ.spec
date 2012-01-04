%global packname  RTAQ
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          RTAQ: Tools for the analysis of trades and quotes in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xts R-timeDate 


BuildRequires:    R-devel tex(latex) R-xts R-timeDate



%description
The Trades and Quotes data of the New York Stock Exchange is a popular
input for the implementation of intraday trading strategies, the
measurement of liquidity and volatility and investigation of the market
microstructure, among others. This package contains a collection of R
functions to carefully clean and match the trades and quotes data,
calculate ex post liquidity and volatility measures and detect price jumps
in the data.

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
%doc %{rlibdir}/RTAQ/html
%doc %{rlibdir}/RTAQ/DESCRIPTION
%doc %{rlibdir}/RTAQ/doc
%{rlibdir}/RTAQ/INDEX
%{rlibdir}/RTAQ/data
%{rlibdir}/RTAQ/R
RPM build errors:
%{rlibdir}/RTAQ/NAMESPACE
%{rlibdir}/RTAQ/libs
%{rlibdir}/RTAQ/Meta
%{rlibdir}/RTAQ/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora