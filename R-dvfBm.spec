%global packname  dvfBm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Discrete variations of a fractional Brownian motion

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-wmtsa 

BuildRequires:    R-devel tex(latex) R-wmtsa 

%description
Hurst exponent estimation of a fractional Brownian motion by using
discrete variations methods in presence of outliers and/or an additive

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
%doc %{rlibdir}/dvfBm/DESCRIPTION
%doc %{rlibdir}/dvfBm/html
%{rlibdir}/dvfBm/Meta
%{rlibdir}/dvfBm/NAMESPACE
%{rlibdir}/dvfBm/help
%{rlibdir}/dvfBm/INDEX
%{rlibdir}/dvfBm/R

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora