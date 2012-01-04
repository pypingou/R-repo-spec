%global packname  plsRglm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.6
Release:          1%{?dist}
Summary:          Partial least squares Regression for generalized linear models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-mvtnorm R-boot 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mvtnorm R-boot 


%description
This package provides Partial least squares Regression for generalized
linear models and kfold crossvalidation of such models using various
criteria. It allows for missing data in the eXplanatory variables.
Bootstrap confidence intervals constructions are also available.

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
%doc %{rlibdir}/plsRglm/DESCRIPTION
%doc %{rlibdir}/plsRglm/CITATION
%doc %{rlibdir}/plsRglm/LICENCE
%doc %{rlibdir}/plsRglm/html
%doc %{rlibdir}/plsRglm/NEWS
%{rlibdir}/plsRglm/help
%{rlibdir}/plsRglm/data
%{rlibdir}/plsRglm/Meta
%{rlibdir}/plsRglm/INDEX
%{rlibdir}/plsRglm/demo
%{rlibdir}/plsRglm/R
%{rlibdir}/plsRglm/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.6-1
- initial package for Fedora