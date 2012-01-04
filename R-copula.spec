%global packname  copula
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Multivariate dependence with copulas

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-mvtnorm R-scatterplot3d R-sn R-pspline 

BuildRequires:    R-devel tex(latex) R-methods R-mvtnorm R-scatterplot3d R-sn R-pspline 

%description
Classes (S4) of commonly used copulas including elliptical (normal and t),
Archimedean (Clayton, Gumbel, Frank, and Ali-Mikhail-Haq), extreme value
(Gumbel, Husler-Reiss, Galambos, Tawn, and t-EV), and other families
(Plackett and Farlie-Gumbel-Morgenstern). Methods for density,
distribution, random number generation, bivariate dependence measures,
perspective and contour plots. Functions for fitting copula models with
variance estimate. Independence tests among random variables and random
vectors. Serial independence tests for univariate and multivariate
continuous time series. Goodness-of-fit tests for copulas based on
multipliers and on the parametric bootstrap. Tests of extreme-value

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.7-1
- initial package for Fedora