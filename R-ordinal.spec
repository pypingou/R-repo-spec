%global packname  ordinal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.09.14
Release:          1%{?dist}
Summary:          Regression Models for Ordinal Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.09-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-ucminf R-Matrix 
Requires:         R-numDeriv 

BuildRequires:    R-devel tex(latex) R-MASS R-ucminf R-Matrix
BuildRequires:    R-numDeriv 


%description
This package implements cumulative link (mixed) models also known as
ordered regression models, proportional odds models, proportional hazards
models for grouped survival times and ordered logit/probit/... models.
Estimation is via maximum likelihood and mixed models are fitted with the
Laplace approximation and adaptive Gauss-Hermite quadrature. Multiple
random effect terms are allowed and they may be nested, crossed or
partially nested/crossed. Restrictions of symmetry and equidistance can be
imposed on the thresholds (cut-points). Standard model methods are
available (summary, anova, drop-methods, step, confint, predict etc.) in
addition to profile methods and slice methods for visualizing the
likelihood function and checking convergence.

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
%doc %{rlibdir}/ordinal/NEWS
%doc %{rlibdir}/ordinal/doc
%doc %{rlibdir}/ordinal/CITATION
%doc %{rlibdir}/ordinal/html
%doc %{rlibdir}/ordinal/DESCRIPTION
%doc %{rlibdir}/ordinal/LICENCE
%{rlibdir}/ordinal/NAMESPACE
%{rlibdir}/ordinal/Meta
%{rlibdir}/ordinal/R
%{rlibdir}/ordinal/libs
%{rlibdir}/ordinal/data
%{rlibdir}/ordinal/INDEX
%{rlibdir}/ordinal/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.09.14-1
- initial package for Fedora