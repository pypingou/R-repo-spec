%global packname  MNP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.2
Release:          1%{?dist}
Summary:          R Package for Fitting the Multinomial Probit Model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-utils 

BuildRequires:    R-devel tex(latex) R-MASS R-utils 

%description
MNP is a publicly available R package that fits the Bayesian multinomial
probit model via Markov chain Monte Carlo. The multinomial probit model is
often used to analyze the discrete choices made by individuals recorded in
survey data. Examples where the multinomial probit model may be useful
include the analysis of product choice by consumers in market research and
the analysis of candidate or party choice by voters in electoral studies. 
The MNP software can also fit the model with different choice sets for
each individual, and complete or partial individual choice orderings of
the available alternatives from the choice set. The estimation is based on
the efficient marginal data augmentation algorithm that is developed by
Imai and van Dyk (2005). ``A Bayesian Analysis of the Multinomial Probit
Model Using the Data Augmentation,'' Journal of Econometrics, Vol. 124,
No. 2 (February), pp. 311-334. Detailed examples are given in Imai and van
Dyk (2005). ``MNP: R Package for Fitting the Multinomial Probit Model.''
Journal of Statistical Software, Vol. 14, No. 3 (May), pp. 1-32.

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
%doc %{rlibdir}/MNP/html
%doc %{rlibdir}/MNP/DESCRIPTION
%{rlibdir}/MNP/NAMESPACE
%{rlibdir}/MNP/R
%{rlibdir}/MNP/help
%{rlibdir}/MNP/data
%{rlibdir}/MNP/INDEX
%{rlibdir}/MNP/libs
%{rlibdir}/MNP/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.2-1
- initial package for Fedora