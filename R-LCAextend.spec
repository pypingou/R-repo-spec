%global packname  LCAextend
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Latent Class Analysis (LCA) with familial dependence in extended pedigrees

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot R-mvtnorm R-rms R-kinship 


BuildRequires:    R-devel tex(latex) R-boot R-mvtnorm R-rms R-kinship



%description
This package performs a Latent Class Analysis of phenotypic measurements
in pedigrees and a model selection based on one of two methods:
likelihood-based cross-validation and Bayesian Information Criterion. It
computes also individual and triplet child-parents weights in a pedigree
using an upward-downward algorithm. It takes into account the familial
dependence defined by the pedigree structure by considering that a class
of a child depends on his parents classes via triplet-transition
probabilities of the classes. The package handles the case where
measurements are available on all subjects and the case where measurements
are available only on symptomatic (i.e. affected) subjects. Distributions
for discrete (or ordinal) and continuous data are currently implemented.
The package can deal with missing data.

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
%doc %{rlibdir}/LCAextend/DESCRIPTION
%doc %{rlibdir}/LCAextend/html
%{rlibdir}/LCAextend/NAMESPACE
%{rlibdir}/LCAextend/Meta
%{rlibdir}/LCAextend/data
%{rlibdir}/LCAextend/R
%{rlibdir}/LCAextend/INDEX
%{rlibdir}/LCAextend/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora