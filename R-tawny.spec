%global packname  tawny
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Provides various portfolio optimization strategies including random matrix theory and shrinkage estimators

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-futile R-futile.logger R-zoo R-xts R-quantmod 

BuildRequires:    R-devel tex(latex) R-futile R-futile.logger R-zoo R-xts R-quantmod 

%description
Portfolio optimization typically requires an estimate of a covariance
matrix of asset returns. There are many approaches for constructing such a
covariance matrix, some using the sample covariance matrix as a starting
point. This package provides implementations for two such methods: random
matrix theory and shrinkage estimation. Each method attempts to clean or
remove noise related to the sampling process from the sample covariance

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora