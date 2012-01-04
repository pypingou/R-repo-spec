%global packname  glmulti
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          GLM model selection and multimodel inference made easy

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-methods 

BuildRequires:    R-devel tex(latex) R-rJava R-methods 

%description
Automated model selection and model-averaging. Provides a wrapper for glm
and similar functions, automatically generating all possible models (under
constraints set by the user) with the specified response and explanatory
variables, and finding the best models in terms of some Information
Criterion (AIC, AICc or BIC). Can handle very large numbers of candidate
models. Features a Genetic Algorithm to find the best models when an
exhaustive screening of the candidates is not feasible.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora