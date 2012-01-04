%global packname  bayesm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.4
Release:          1%{?dist}
Summary:          Bayesian Inference for Marketing/Micro-econometrics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
bayesm covers many important models used in marketing and
micro-econometrics applications. The package includes: Bayes Regression
(univariate or multivariate dep var), Bayes Seemingly Unrelated Regression
(SUR), Binary and Ordinal Probit, Multinomial Logit (MNL) and Multinomial
Probit (MNP), Multivariate Probit, Negative Binomial (Poisson) Regression,
Multivariate Mixtures of Normals (including clustering), Dirichlet Process
Prior Density Estimation with normal base, Hierarchical Linear Models with
normal prior and covariates, Hierarchical Linear Models with a mixture of
normals prior and covariates, Hierarchical Multinomial Logits with a
mixture of normals prior and covariates, Hierarchical Multinomial Logits
with a Dirichlet Process prior and covariates, Hierarchical Negative
Binomial Regression Models, Bayesian analysis of choice-based conjoint
data, Bayesian treatment of linear instrumental variables models, and
Analysis of Multivariate Ordinal survey data with scale usage
heterogeneity (as in Rossi et al, JASA (01)). For further reference,
consult our book, Bayesian Statistics and Marketing by Rossi, Allenby and

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.4-1
- initial package for Fedora