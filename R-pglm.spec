%global packname  pglm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          panel generalized linear model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-maxLik R-statmod R-plm 


BuildRequires:    R-devel tex(latex) R-maxLik R-statmod R-plm



%description
Estimation of panel models for glm-like models: this includes binomial
models (logit and probit) count models (poisson and negbin) and ordered
models (logit and probit)

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
%doc %{rlibdir}/pglm/DESCRIPTION
%doc %{rlibdir}/pglm/html
%{rlibdir}/pglm/R
%{rlibdir}/pglm/data
%{rlibdir}/pglm/NAMESPACE
%{rlibdir}/pglm/help
%{rlibdir}/pglm/Meta
%{rlibdir}/pglm/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora