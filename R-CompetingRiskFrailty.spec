%global packname  CompetingRiskFrailty
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Competing Risk Model with Frailties for Right Censored Survival Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package offers a fitting of smooth varying coefficients in a competing
risks modelling of hazards as well as estimating of the frailties (or
unobserved heterogenities) for clustered observations. Nonparametric
penalized spline (p-spline) fitting of smooth covariates effects is
proposed. As a spline basis truncated polynomial functions are chosen. The
frailties are also fitted (via the EM-algoritghm) in a flexible way using
a penalizied mixture of gamma distributions.

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
%doc %{rlibdir}/CompetingRiskFrailty/doc
%doc %{rlibdir}/CompetingRiskFrailty/html
%doc %{rlibdir}/CompetingRiskFrailty/DESCRIPTION
%{rlibdir}/CompetingRiskFrailty/Meta
%{rlibdir}/CompetingRiskFrailty/data
%{rlibdir}/CompetingRiskFrailty/R
%{rlibdir}/CompetingRiskFrailty/NAMESPACE
%{rlibdir}/CompetingRiskFrailty/help
%{rlibdir}/CompetingRiskFrailty/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora