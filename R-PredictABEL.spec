%global packname  PredictABEL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Assessment of risk prediction models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-ROCR R-epitools R-PBSmodelling 


BuildRequires:    R-devel tex(latex) R-Hmisc R-ROCR R-epitools R-PBSmodelling



%description
PredictABEL includes functions to assess the performance of risk models.
The package contains functions for the various measures that are used in
empirical studies, including univariate and multivariate odds ratios (OR)
of the predictors, the c-statistic (or area under the receiver operating
characteristic (ROC) curve (AUC)), Hosmer-Lemeshow goodness of fit test,
reclassification table, net reclassification improvement (NRI) and
integrated discrimination improvement (IDI). Also included are functions
to create plots, such as risk distributions, ROC curves, calibration plot,
discrimination box plot and predictiveness curves. In addition to
functions to assess the performance of risk models, the package includes
functions to obtain weighted and unweighted risk scores as well as
predicted risks using logistic regression analysis. These logistic
regression functions are specifically written for models that include
genetic variables, but they can also be applied to models that are based
on non-genetic risk factors only.  Finally, the package includes function
to construct a simulated dataset that contains individual genotype data,
estimated genetic risk, and disease status, used for the evaluation of
genetic risk models.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora