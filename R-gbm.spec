%global packname  gbm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.3.1
Release:          1%{?dist}
Summary:          Generalized Boosted Regression Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-3.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-lattice R-splines 

BuildRequires:    R-devel tex(latex) R-survival R-lattice R-splines 

%description
This package implements extensions to Freund and Schapire's AdaBoost
algorithm and Friedman's gradient boosting machine. Includes regression
methods for least squares, absolute loss, quantile regression, logistic,
Poisson, Cox proportional hazards partial likelihood, and AdaBoost
exponential loss.

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
%doc %{rlibdir}/gbm/DESCRIPTION
%doc %{rlibdir}/gbm/doc
%doc %{rlibdir}/gbm/html
%{rlibdir}/gbm/demo
%{rlibdir}/gbm/R
%{rlibdir}/gbm/NAMESPACE
%{rlibdir}/gbm/LICENSE
%{rlibdir}/gbm/INDEX
%{rlibdir}/gbm/Meta
%{rlibdir}/gbm/libs
%{rlibdir}/gbm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.3.1-1
- initial package for Fedora