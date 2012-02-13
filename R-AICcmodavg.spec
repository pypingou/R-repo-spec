%global packname  AICcmodavg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.24
Release:          1%{dist}
Summary:          Model selection and multimodel inference based on (Q)AIC(c)

Group:            Applications/Engineering 
License:          GPL (>= 2 )
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
This package includes functions to create model selection tables based on
Akaike's information criterion (AIC) and the second-order AIC (AICc), as
well as their quasi-likelihood counterparts (QAIC, QAICc).  Tables are
printed with delta AIC and Akaike weights.  The package also features
functions to conduct classic model averaging (multimodel inference) for a
given parameter of interest or predicted values, as well as a shrinkage
version of model averaging parameter estimates.  Other handy functions
enable the computation of relative variable importance, evidence ratios,
and confidence sets for the best model.  The present version works with
linear models ('lm' class), generalized linear models ('glm' class),
linear models fit by generalized least squares ('gls' class), linear mixed
models ('lme' class), generalized linear mixed models ('mer' class),
multinomial and ordinal logistic regressions ('multinom' and 'polr'
classes), and nonlinear models ('nls' class).  The package also supports
various models incorporating detection probabilities such as single-season
occupancy models ('unmarkedFitOccu' class), multiple-season occupancy
models ('unmarkedFitColExt' class), single-season heterogeneity models
('unmarkedFitOccuRN' class), and single-season and multiple-season
N-mixture models for repeated counts ('unmarkedFitPCount' and
'unmarkedFitPCO' classes, respectively).

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
%doc %{rlibdir}/AICcmodavg/DESCRIPTION
%doc %{rlibdir}/AICcmodavg/CITATION
%doc %{rlibdir}/AICcmodavg/html
%doc %{rlibdir}/AICcmodavg/NEWS
%{rlibdir}/AICcmodavg/R
%{rlibdir}/AICcmodavg/INDEX
%{rlibdir}/AICcmodavg/data
%{rlibdir}/AICcmodavg/NAMESPACE
%{rlibdir}/AICcmodavg/Meta
%{rlibdir}/AICcmodavg/help

%changelog
* Mon Feb 13 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24-1
- Update to version 1.24

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.21-1
- initial package for Fedora