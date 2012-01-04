%global packname  bujar
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Buckley-James Regression for Survival Data with High-Dimensional Covariates

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gbm R-mboost R-mda R-earth R-lars R-elasticnet 


BuildRequires:    R-devel tex(latex) R-gbm R-mboost R-mda R-earth R-lars R-elasticnet



%description
Buckley-James regression for right-censoring survival data with
high-dimensional covariates. Including L_2 boosting with componentwise
linear least squares, componentwise smoothing splines, P-splines,
regression trees and boosted MARS. Other high-dimensional tools include
elastic net, MARS, ACOSSO.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora