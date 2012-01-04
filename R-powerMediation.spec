%global packname  powerMediation
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Power/Sample size calculation for mediation analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
The package contains functions for calculating power, sample size, and
minimal detectable mediation effect for testing mediation effect in
linear, logistic, poisson, or cox regression. The package also contains
functions for calculating power, sample size, and minimal detectable slope
for testing the slope in a simple linear regression (only one predictor).

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
%doc %{rlibdir}/powerMediation/html
%doc %{rlibdir}/powerMediation/DESCRIPTION
%{rlibdir}/powerMediation/NAMESPACE
%{rlibdir}/powerMediation/help
%{rlibdir}/powerMediation/R
%{rlibdir}/powerMediation/Meta
%{rlibdir}/powerMediation/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.7-1
- initial package for Fedora