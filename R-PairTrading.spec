%global packname  PairTrading
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          classical pair trading based on cointegration in finance

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xts R-tseries 


BuildRequires:    R-devel tex(latex) R-xts R-tseries



%description
This package gives classical trading strategy called "Pair trading" to
you. you can easily specify pairs for trading and do back-test by this
package. It's based on cointegration. Cointegration is a statistical
feature of time series proposed by Engle and Granger.

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
%doc %{rlibdir}/PairTrading/DESCRIPTION
%doc %{rlibdir}/PairTrading/doc
%doc %{rlibdir}/PairTrading/html
%{rlibdir}/PairTrading/help
%{rlibdir}/PairTrading/NAMESPACE
%{rlibdir}/PairTrading/data
%{rlibdir}/PairTrading/R
RPM build errors:
%{rlibdir}/PairTrading/Meta
%{rlibdir}/PairTrading/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora