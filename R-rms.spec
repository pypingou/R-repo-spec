%global packname  rms
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.3.2
Release:          1%{?dist}
Summary:          Regression Modeling Strategies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Hmisc R-survival 

BuildRequires:    R-devel tex(latex) R-Hmisc R-survival 

%description
Regression modeling, testing, estimation, validation, graphics,
prediction, and typesetting by storing enhanced model design attributes in
the fit.  rms is a collection of 229 functions that assist with and
streamline modeling.  It also contains functions for binary and ordinal
logistic regression models and the Buckley-James multiple regression model
for right-censored responses, and implements penalized maximum likelihood
estimation for logistic and ordinary linear models.  rms works with almost
any regression model, but it was especially written to work with binary or
ordinal logistic regression, Cox regression, accelerated failure time
models, ordinary linear models,	the Buckley-James model, generalized least
squares for serially or spatially correlated observations, generalized
linear models, and quantile regression.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.3.2-1
- initial package for Fedora