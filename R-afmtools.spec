%global packname  afmtools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Estimation, Diagnostic and Forecasting Functions for ARFIMA models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-polynom R-fracdiff R-hypergeo R-sandwich R-longmemo 

BuildRequires:    R-devel tex(latex) R-polynom R-fracdiff R-hypergeo R-sandwich R-longmemo 

%description
A collection of estimation, forecasting and diagnostic tools for
autoregressive fractionally integrated moving-average process (ARFIMA).

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
%doc %{rlibdir}/afmtools/html
%doc %{rlibdir}/afmtools/DESCRIPTION
%doc %{rlibdir}/afmtools/CITATION
%{rlibdir}/afmtools/R
%{rlibdir}/afmtools/NAMESPACE
%{rlibdir}/afmtools/INDEX
%{rlibdir}/afmtools/Meta
%{rlibdir}/afmtools/data
%{rlibdir}/afmtools/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora