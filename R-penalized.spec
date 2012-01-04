%global packname  penalized
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.37
Release:          1%{?dist}
Summary:          L1 (lasso) and L2 (ridge) penalized estimation in GLMs and in the Cox model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-37.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-survival 

BuildRequires:    R-devel tex(latex) R-methods R-survival 

%description
A package for fitting possibly high dimensional penalized regression
models. The penalty structure can be any combination of an L1 penalty
(lasso), an L2 penalty (ridge) and a positivity constraint on the
regression coefficients. The supported regression models are linear,
logistic and poisson regression and the Cox Proportional Hazards model.
Cross-validation routines allow optimization of the tuning parameters.

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
%doc %{rlibdir}/penalized/doc
%doc %{rlibdir}/penalized/html
%doc %{rlibdir}/penalized/CITATION
%doc %{rlibdir}/penalized/DESCRIPTION
%{rlibdir}/penalized/NAMESPACE
%{rlibdir}/penalized/Meta
%{rlibdir}/penalized/data
%{rlibdir}/penalized/R
%{rlibdir}/penalized/INDEX
%{rlibdir}/penalized/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.37-1
- initial package for Fedora