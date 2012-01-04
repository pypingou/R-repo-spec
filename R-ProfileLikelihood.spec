%global packname  ProfileLikelihood
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Profile Likelihood for a Parameter in Commonly Used Statistical Models

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme R-MASS 

BuildRequires:    R-devel tex(latex) R-nlme R-MASS 

%description
This package provides profile likelihoods for a parameter of interest in
commonly used statistical models. The models include linear models,
generalized linear models, proportional odds models, linear mixed-effects
models, and linear models for longitudinal responses fitted by generalized
least squares. The package also provides plots for normalized profile
likelihoods as well as the maximum profile likelihood estimates and the
kth likelihood support intervals.

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
%doc %{rlibdir}/ProfileLikelihood/html
%doc %{rlibdir}/ProfileLikelihood/DESCRIPTION
%{rlibdir}/ProfileLikelihood/data
%{rlibdir}/ProfileLikelihood/R
%{rlibdir}/ProfileLikelihood/Meta
%{rlibdir}/ProfileLikelihood/INDEX
%{rlibdir}/ProfileLikelihood/help
%{rlibdir}/ProfileLikelihood/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora