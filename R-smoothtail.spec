%global packname  smoothtail
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Smooth Estimation of GPD Shape Parameter

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-logcondens 

BuildRequires:    R-devel tex(latex) R-logcondens 

%description
Given independent and identically distributed observations X(1), ..., X(n)
from a Generalized Pareto distribution with shape parameter gamma in
[-1,0], this package offers several estimates to compute estimates of
gamma. The estimates are based on the principle of replacing the order
statistics by quantiles of a distribution function based on a log--concave
density function. This procedure is justified by the fact that the GPD
density is log--concave for gamma in [-1,0].

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
%doc %{rlibdir}/smoothtail/DESCRIPTION
%doc %{rlibdir}/smoothtail/html
%{rlibdir}/smoothtail/R
%{rlibdir}/smoothtail/Meta
%{rlibdir}/smoothtail/help
%{rlibdir}/smoothtail/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora