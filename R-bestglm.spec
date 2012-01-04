%global packname  bestglm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.33
Release:          1%{?dist}
Summary:          Best Subset GLM

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-leaps R-lars R-ElemStatLearn 

BuildRequires:    R-devel tex(latex) R-leaps R-lars R-ElemStatLearn 

%description
Best subset glm using AIC, BIC, EBIC, BICq or Cross-Validation. For the
normal case, the 'leaps' is used. Otherwise, a slower exhaustive search.
The 'xtable' package is needed for vignette 'SimExperimentBICq.Rnw'
accompanying this package.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.33-1
- initial package for Fedora