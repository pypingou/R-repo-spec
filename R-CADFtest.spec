%global packname  CADFtest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          This package performs the CADF unit root test proposed in Hansen (1995).

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-dynlm R-sandwich R-tseries R-urca 


BuildRequires:    R-devel tex(latex) R-dynlm R-sandwich R-tseries R-urca



%description
This package performs Hansen's (1995) Covariate-Augmented Dickey-Fuller
(CADF) test. The only required argument is y, the Tx1 time series to be
tested. If no stationary covariate X is passed to the procedure, then an
ordinary ADF test is performed. The p-values of the test are computed
using a procedure proposed in Costantini, Lupi and Popp (2007),
illustrated in Lupi (2009).

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora