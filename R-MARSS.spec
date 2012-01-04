%global packname  MARSS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.7
Release:          1%{?dist}
Summary:          Multivariate Autoregressive State-Space Modeling

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-mvtnorm R-nlme R-time R-KFAS 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm R-nlme R-time R-KFAS 

%description
The MARSS package provides maximum-likelihood parameter estimation for
constrained and unconstrained linear multivariate autoregressive
state-space (MARSS) models fit to multivariate time-series data.  Fitting
is primarily via an Expectation-Maximization (EM) algorithm, although
fitting via the BFGS algorithm (using the optim function) is also
provided. MARSS models are a class of dynamic linear model (DLM) and
vector autoregressive model (VAR) model.  Functions are provided for
parametric and innovations bootstrapping, Kalman filtering and smoothing,
bootstrap model selection criteria (AICb), confidences intervals via the
hessian approximation and via bootstrapping and calculation of auxilliary
residuals for detecting outliers and shocks.  The user guide shows
examples of using MARSS for parameter estimation for a variety of
applications, model selection, dynamic factor analysis, outlier and shock
detection, and addition of covariates.  Type RShowDoc("UserGuide",
package="MARSS") at the R command line to open the MARSS user guide.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.7-1
- initial package for Fedora