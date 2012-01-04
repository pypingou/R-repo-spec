%global packname  glmnet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.1
Release:          1%{?dist}
Summary:          Lasso and elastic-net regularized generalized linear models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-utils 

BuildRequires:    R-devel tex(latex) R-Matrix R-utils 

%description
Extremely efficient procedures for fitting the entire lasso or elastic-net
regularization path for linear regression, logistic and multinomial
regression models, poisson regression and the Cox model. The algorithm
uses cyclical coordinate descent in a pathwise fashion, as described in
the paper listed below.

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
%doc %{rlibdir}/glmnet/html
%doc %{rlibdir}/glmnet/DESCRIPTION
%doc %{rlibdir}/glmnet/CITATION
%doc %{rlibdir}/glmnet/doc
%{rlibdir}/glmnet/INDEX
%{rlibdir}/glmnet/NAMESPACE
%{rlibdir}/glmnet/Meta
%{rlibdir}/glmnet/libs
%{rlibdir}/glmnet/R
RPM build errors:
%{rlibdir}/glmnet/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.1-1
- initial package for Fedora