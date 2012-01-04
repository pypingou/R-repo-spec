%global packname  SkewHyperbolic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          The Skew Hyperbolic Student t-distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DistributionUtils R-GeneralizedHyperbolic 

BuildRequires:    R-devel tex(latex) R-DistributionUtils R-GeneralizedHyperbolic 

%description
Functions are provided for the density function, distribution function,
quantiles and random number generation for the skew hyperbolic
t-distribution. There are also functions that fit the distribution to
data. There are functions for the mean, variance, skewness, kurtosis and
mode of a given distribution and to calculate moments of any order about
any centre. To assess goodness of fit, there are functions to generate a
Q-Q plot and a P-P plot.

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
%doc %{rlibdir}/SkewHyperbolic/html
%doc %{rlibdir}/SkewHyperbolic/DESCRIPTION
%{rlibdir}/SkewHyperbolic/unitTests
%{rlibdir}/SkewHyperbolic/R
%{rlibdir}/SkewHyperbolic/NAMESPACE
%{rlibdir}/SkewHyperbolic/data
%{rlibdir}/SkewHyperbolic/help
%{rlibdir}/SkewHyperbolic/Meta
%{rlibdir}/SkewHyperbolic/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora