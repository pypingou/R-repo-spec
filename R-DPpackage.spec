%global packname  DPpackage
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Bayesian Nonparametric and Semiparametric Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-nlme 

BuildRequires:    R-devel tex(latex) R-MASS R-nlme 

%description
This package contains functions to perform inference via simulation from
the posterior distributions for Bayesian nonparametric and semiparametric
models. Although the name of the package was motivated by the Dirichlet
Process prior, the package considers and will consider other priors on
functional spaces. So far, DPpackage includes models considering Dirichlet
Processes, Dependent Dirichlet Processes, Dependent Poisson- Dirichlet
Processes, Hierarchical Dirichlet Processes, Polya Trees, Mixtures of
Triangular distributions, and Random Bernstein polynomials priors. The
package also includes models considering Penalized B-Splines. Currently
the package includes semiparametric models for marginal and conditional
density estimation, ROC curve analysis, interval censored data, binary
regression models, generalized linear mixed models, IRT type models, and
generalized additive models. The package also contains functions to
compute Pseudo-Bayes factors for model comparison, and to elicitate the
precision parameter of the Dirichlet Process. To maximize computational
efficiency, the actual sampling for each model is done in compiled
FORTRAN. The functions return objects which can be subsequently analyzed
with functions provided in the coda package.

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
%doc %{rlibdir}/DPpackage/DESCRIPTION
%doc %{rlibdir}/DPpackage/html
%doc %{rlibdir}/DPpackage/CITATION
%{rlibdir}/DPpackage/help
%{rlibdir}/DPpackage/Meta
%{rlibdir}/DPpackage/libs
%{rlibdir}/DPpackage/LICENSE
%{rlibdir}/DPpackage/R
RPM build errors:
%{rlibdir}/DPpackage/NAMESPACE
%{rlibdir}/DPpackage/data
%{rlibdir}/DPpackage/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora