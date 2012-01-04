%global packname  SemiParBIVProbit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.4.1
Release:          1%{?dist}
Summary:          Semiparametric Bivariate Probit Modelling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-4.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-VGAM R-trust R-mgcv R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-VGAM R-trust R-mgcv R-mvtnorm 

%description
Routine for bivariate probit modelling with semiparametric predictors,
including linear and nonlinear effects, in the presence of correlated
error equations, endogeneity or sample selection.

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
%doc %{rlibdir}/SemiParBIVProbit/DESCRIPTION
%doc %{rlibdir}/SemiParBIVProbit/html
%{rlibdir}/SemiParBIVProbit/INDEX
%{rlibdir}/SemiParBIVProbit/help
%{rlibdir}/SemiParBIVProbit/Meta
%{rlibdir}/SemiParBIVProbit/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.4.1-1
- initial package for Fedora