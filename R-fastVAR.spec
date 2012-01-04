%global packname  fastVAR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          fastVAR

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-glmnet 

BuildRequires:    R-devel tex(latex) R-glmnet 

%description
This package is designed for time series data.  Uses fast implementations
to estimate Vector Autoregressive models and Vector Autoregressive models
with Exogenous Inputs.  For speedup, fastVAR can use multiple cpu cores to
calculate the estimates.  For very large systems, fastVAR uses Lasso
penalty to return very sparse coefficient matrices. Regression diagnostics
can be used to compare models, and prediction functions can be used to
calculate the n-step ahead prediction. Map-Reduce functions are in the
works (Beta) for estimating large VAR models on a compute cluster.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora