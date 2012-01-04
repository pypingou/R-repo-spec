%global packname  CompModSA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Sensitivity Analysis for Complex Computer Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-quadprog R-tgp R-gam R-locfit R-rpart R-mda R-corpcor R-randomForest R-gbm R-MASS R-mlegp R-polspline R-fields R-methods R-lars 


BuildRequires:    R-devel tex(latex) R-quadprog R-tgp R-gam R-locfit R-rpart R-mda R-corpcor R-randomForest R-gbm R-MASS R-mlegp R-polspline R-fields R-methods R-lars



%description
Uses regression surface approximations to calculate variance decomposition
and total variance sensitivity indices. This package is useful for
conducting sensitivity analysis of complex computer codes when model
evaluations are somewhat expensive (e.g. take longer than a couple seconds
to run) but a reasonable number (50 or more) of model evaluations can be
obtained at sampled input values.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora