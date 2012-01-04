%global packname  plsRcox
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Partial least squares Regression for Cox models and related techniques

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-boot R-plsRglm R-lars R-survival R-pls 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-boot R-plsRglm R-lars R-survival R-pls 


%description
This packages provides Partial least squares Regression and various
techniques for fitting Cox models in high dimensionnal settings. It allows
for Kfold crossvalidation of such models using various criteria, missing
data in the eXplanatory variables. Bootstrap confidence intervals
constructions are also available.

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
%doc %{rlibdir}/plsRcox/DESCRIPTION
%doc %{rlibdir}/plsRcox/CITATION
%doc %{rlibdir}/plsRcox/LICENCE
%doc %{rlibdir}/plsRcox/html
%doc %{rlibdir}/plsRcox/NEWS
%{rlibdir}/plsRcox/demo
%{rlibdir}/plsRcox/data
%{rlibdir}/plsRcox/Meta
%{rlibdir}/plsRcox/R
%{rlibdir}/plsRcox/help
%{rlibdir}/plsRcox/INDEX
%{rlibdir}/plsRcox/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora