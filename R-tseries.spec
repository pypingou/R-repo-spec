%global packname  tseries
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.10.27
Release:          1%{?dist}
Summary:          Time series analysis and computational finance

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.10-27.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quadprog R-stats R-zoo 

BuildRequires:    R-devel tex(latex) R-quadprog R-stats R-zoo 

%description
Package for time series analysis and computational finance

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
%doc %{rlibdir}/tseries/html
%doc %{rlibdir}/tseries/CITATION
%doc %{rlibdir}/tseries/DESCRIPTION
%{rlibdir}/tseries/R
%{rlibdir}/tseries/libs
%{rlibdir}/tseries/NAMESPACE
%{rlibdir}/tseries/help
%{rlibdir}/tseries/data
%{rlibdir}/tseries/Meta
%{rlibdir}/tseries/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10.27-1
- initial package for Fedora