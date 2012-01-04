%global packname  dhglm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Double Hierarchical Generalized Linear Models

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix R-numDeriv R-boot 

BuildRequires:    R-devel tex(latex) R-Matrix R-numDeriv R-boot 

%description
The dhglm package fits double hierarchical generalized linear models in
which the mean, dispersion parameters for variance of random effects, and
residual variance (overdispersion) can be further modeled as random-effect

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
%doc %{rlibdir}/dhglm/html
%doc %{rlibdir}/dhglm/DESCRIPTION
%{rlibdir}/dhglm/NAMESPACE
%{rlibdir}/dhglm/Meta
%{rlibdir}/dhglm/R
%{rlibdir}/dhglm/INDEX
%{rlibdir}/dhglm/data
%{rlibdir}/dhglm/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora