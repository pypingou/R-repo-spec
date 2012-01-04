%global packname  GOFSN
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Goodness-of-fit tests for the family of skew-normal models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sn 


BuildRequires:    R-devel tex(latex) R-sn



%description
GOFSN is a package that implements a method for checking if a skew-normal
model fits the observed dataset, when all parameters are unknown. While
location and scale parameters are estimated by moment estimators, the
shape parameter is integrated with respect to the prior predictive
distribution, as proposed in (BOX, 1980). A default and proper prior on
skewness parameter is used to obtain the prior predictive distribution, as
proposed in (CABRAS, CASTELLANOS, 2008). Goodness-of-fit tests, here
proposed, depend only on sample size and exhibit full agreement between
nominal and actual size. This package implements EDF statistics
Kolmogorov-Smirnov(D), Cram\'er-von Mises(W2) and proposes some simple
algorithms (SimulD,SimulW2) to approximate their respective marginal
predictive distributions. It also has functions (ks.sn,W2.sn) that
calculate the p-value on observed data.

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
%doc %{rlibdir}/GOFSN/html
%doc %{rlibdir}/GOFSN/DESCRIPTION
%{rlibdir}/GOFSN/help
%{rlibdir}/GOFSN/R
%{rlibdir}/GOFSN/INDEX
%{rlibdir}/GOFSN/NAMESPACE
%{rlibdir}/GOFSN/data
%{rlibdir}/GOFSN/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora