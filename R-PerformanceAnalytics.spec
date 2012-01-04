%global packname  PerformanceAnalytics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3.2
Release:          1%{?dist}
Summary:          Econometric tools for performance and risk analysis.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-zoo R-xts 


BuildRequires:    R-devel tex(latex) R-zoo R-xts



%description
Collection of econometric functions for performance and risk analysis.
This package aims to aid practitioners and researchers in utilizing the
latest research in analysis of non-normal return streams.  In general, it
is most tested on return (rather than price) data on a regular scale, but
most functions will work with irregular return data as well, and
increasing numbers of functions will work with P&L or price data where

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
%doc %{rlibdir}/PerformanceAnalytics/DESCRIPTION
%doc %{rlibdir}/PerformanceAnalytics/doc
%doc %{rlibdir}/PerformanceAnalytics/html
%doc %{rlibdir}/PerformanceAnalytics/NEWS
%{rlibdir}/PerformanceAnalytics/NAMESPACE
%{rlibdir}/PerformanceAnalytics/Meta
%{rlibdir}/PerformanceAnalytics/R
%{rlibdir}/PerformanceAnalytics/help
%{rlibdir}/PerformanceAnalytics/INDEX
%{rlibdir}/PerformanceAnalytics/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3.2-1
- initial package for Fedora