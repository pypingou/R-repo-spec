%global packname  sspir
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.8
Release:          1%{?dist}
Summary:          State Space Models in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm 

%description
A glm-like formula language to define dynamic generalized linear models
(state space models). Includes functions for Kalman filtering and
smoothing. Estimation of variance matrices can be perfomred using the EM
algorithm in case of Gaussian models. Read help(sspir) to get started.

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
%doc %{rlibdir}/sspir/html
%doc %{rlibdir}/sspir/DESCRIPTION
%{rlibdir}/sspir/Meta
%{rlibdir}/sspir/demo
%{rlibdir}/sspir/NAMESPACE
%{rlibdir}/sspir/help
%{rlibdir}/sspir/data
%{rlibdir}/sspir/INDEX
%{rlibdir}/sspir/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.8-1
- initial package for Fedora