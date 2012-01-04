%global packname  splinesurv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.14
Release:          1%{?dist}
Summary:          Nonparametric bayesian survival analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-survival 

BuildRequires:    R-devel tex(latex) R-MASS R-survival 

%description
Utilities for nonparametric Bayesian analysis of clustered survival data.
The baseline hazard function and frailty density are modeled using
penalized B-splines. Options include adaptive knot selection and the
inclusion of a parametric component.

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
%doc %{rlibdir}/splinesurv/DESCRIPTION
%doc %{rlibdir}/splinesurv/html
%{rlibdir}/splinesurv/help
%{rlibdir}/splinesurv/Meta
%{rlibdir}/splinesurv/NAMESPACE
%{rlibdir}/splinesurv/libs
%{rlibdir}/splinesurv/R
%{rlibdir}/splinesurv/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.14-1
- initial package for Fedora