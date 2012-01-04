%global packname  ClinicalRobustPriors
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.2
Release:          1%{?dist}
Summary:          Robust Bayesian Priors in Clinical Trials: An R Package for Practitioners

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
In a recent paper, Fuquene, Cook, & Pericchi (2008)
(http://www.bepress.com/mdandersonbiostat/paper44 ) make a comprehensive
proposal putting forward robust, heavy-tailed priors over conjugate,
light-tailed priors in Bayesian analysis. The behavior of Robust Bayesian
methods is qualitative different than Conjugate and short tailed Bayesian
methods and arguably much more reasonable and acceptable to the
practitioner and regulatory agencies. This package is useful to compute
the distributions (prior, likelihood and posterior) and moments of the
robust models: Cauchy/Binomial, Cauchy/Normal and Berger/Normal. Both,
Binomial and Normal Likelihoods can be handled by the software.
Furthermore, the assessment of the hyperparameters and the posterior
analysis can be processed.

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
%doc %{rlibdir}/ClinicalRobustPriors/DESCRIPTION
%doc %{rlibdir}/ClinicalRobustPriors/html
%{rlibdir}/ClinicalRobustPriors/Meta
%{rlibdir}/ClinicalRobustPriors/INDEX
%{rlibdir}/ClinicalRobustPriors/R
%{rlibdir}/ClinicalRobustPriors/NAMESPACE
%{rlibdir}/ClinicalRobustPriors/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.2-1
- initial package for Fedora