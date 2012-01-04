%global packname  mboost
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Model-Based Boosting

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
Functional gradient descent algorithm (boosting) for optimizing general
risk functions utilizing component-wise (penalised) least squares
estimates or regression trees as base-learners for fitting generalized
linear, additive and interaction models to potentially high-dimensional

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
%doc %{rlibdir}/mboost/NEWS
%doc %{rlibdir}/mboost/html
%doc %{rlibdir}/mboost/doc
%doc %{rlibdir}/mboost/CITATION
%doc %{rlibdir}/mboost/DESCRIPTION
%{rlibdir}/mboost/data
%{rlibdir}/mboost/CHANGES
%{rlibdir}/mboost/india_rqss.R
%{rlibdir}/mboost/india_additive.R
%{rlibdir}/mboost/india_plots.R
%{rlibdir}/mboost/india_rqssResults.R
%{rlibdir}/mboost/Meta
%{rlibdir}/mboost/India_quantiles.R
%{rlibdir}/mboost/india_fit.R
%{rlibdir}/mboost/mboost_Bioinf.R
%{rlibdir}/mboost/india_analysis.R
%{rlibdir}/mboost/india_summary.R
%{rlibdir}/mboost/india_blackboost.R
%{rlibdir}/mboost/libs
%{rlibdir}/mboost/R
%{rlibdir}/mboost/INDEX
%{rlibdir}/mboost/cache
%{rlibdir}/mboost/birds_Biometrics.R
%{rlibdir}/mboost/india_vcm.R
%{rlibdir}/mboost/india_stumps.R
%{rlibdir}/mboost/india_preproc.R
%{rlibdir}/mboost/india_helpfunc.R
%{rlibdir}/mboost/NAMESPACE
%{rlibdir}/mboost/india_rqss_lambdaOptFunc.R
%{rlibdir}/mboost/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora