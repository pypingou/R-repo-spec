%global packname  BayesQTLBIC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Bayesian multi-locus QTL analysis based on the BIC criterion

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-leaps 

BuildRequires:    R-devel tex(latex) R-leaps 

%description
R package for a non-MCMC approximate multilocus Bayesian model selection
approach to the analysis of quantitative trait loci (QTL).  The method and
models are described in (Ball, R. D. Genetics 159: 1351--1364, 2001;
http://www.genetics.org/cgi/content/abstract/159/3/1351).  Data is assumed
to be from a QTL mapping family with DNA markers genotyped along the
genome. The QTL mapping problem is represented as a model selection
problem, where each model is a linear regression of the trait on a
selected set of marker values. The main function bicreg.qtl() is based on
the S function bicreg()--- posterior probabilities for models are
approximated from the BIC criterion, calculated for each model in a search
of model space using leaps or regsubsets. Additionally, we allow for prior
probabilities based on expected numbers of QTL per genome and options to
control the size of models considered, and to allow for selectivly
genotyping from the tails of the phenotypic distribution. Missing values
are estimated by multiple imputation, and estimates of marker effects can
be obtained conditional on selection or unconditional and free of
selection bias.  The method relies on 3 approximations: (1.) QTL
configuration is represented approximately by configurations with QTL
located at marker positions; (2.) Posterior probabilities are given
approximately in terms of the BIC criterion; and (3.) The distribution of
missing marker values is approximated by multiple imputation, sampling
from the distribution of missing values conditional on non-missing values.
We have found these are good approximations provided (1.) the marker
spacing is reasonable (less than 30cM); (2.) the sample size is 100 or
more for fully genotyped populations; and (3.) around 10 imputations are
used and the effect of any given QTL on the trait is not large. Due to
limits on the number of markers that can be considered simultaneously the
method is generally applied separately to each chromosome or could be
iteratively applied to sets of chromosomes using fixed sets of predictors
from other chromsomes when analysing a given chromosome.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora