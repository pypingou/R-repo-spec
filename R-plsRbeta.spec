%global packname  plsRbeta
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Partial least squares Regression for beta regression models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-plsRglm 
Requires:         R-mvtnorm R-boot R-Formula R-plsdof 

BuildRequires:    R-devel tex(latex) R-plsRglm
BuildRequires:    R-mvtnorm R-boot R-Formula R-plsdof 


%description
This package provides Partial least squares Regression for beta regression
models and kfold crossvalidation of such models using various criteria. It
allows for missing data in the eXplanatory variables. Bootstrap confidence
intervals constructions are also available.

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
%doc %{rlibdir}/plsRbeta/LICENCE
%doc %{rlibdir}/plsRbeta/html
%doc %{rlibdir}/plsRbeta/DESCRIPTION
%doc %{rlibdir}/plsRbeta/NEWS
%doc %{rlibdir}/plsRbeta/CITATION
%{rlibdir}/plsRbeta/help
%{rlibdir}/plsRbeta/INDEX
%{rlibdir}/plsRbeta/Meta
%{rlibdir}/plsRbeta/R
%{rlibdir}/plsRbeta/NAMESPACE
%{rlibdir}/plsRbeta/demo

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora