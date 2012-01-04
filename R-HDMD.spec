%global packname  HDMD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Statistical Analysis Tools for High Dimension Molecular Data (HDMD)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-psych R-MASS R-base 

BuildRequires:    R-devel tex(latex) R-psych R-MASS R-base 

%description
High Dimensional Molecular Data (HDMD) typically have many more variables
or dimensions than observations or replicates (D>>N).  This can cause many
statistical procedures to fail, become intractable, or produce misleading
results.  This package provides several tools to reduce dimensionality and
analyze biological data for meaningful interpretation of results. Factor
Analysis (FA), Principal Components Analysis (PCA) and Discriminant
Analysis (DA) are frequently used multivariate techniques.  However, PCA
methods \code{\link{prcomp}} and \code{\link{princomp}} do not reflect the
proportion of total variation of each principal component.
\code{\link{Loadings.variation}} displays the relative and cumulative
contribution of variation for each component by accounting for all
variability in data. When D>>N, the maximum likelihood method cannot be
applied in FA and the the principal axes method must be used instead, as
in \code{\link{factor.pa}} of the \code{\link{psych}} package. The
\code{\link{factor.pa.ginv}} function in this package further allows for a
singular covariance matrix by applying a general inverse method to
estimate factor scores.  Moreover, \code{\link{factor.pa.ginv}} removes
and warns of any variables that are constant, which would otherwise create
an invalid covariance matrix. \code{\link{Promax.only}} further allows
users to define rotation parameters during factor estimation. Similar to
the Euclidean distance, the Mahalanobis distance estimates the
relationship among groups. \code{\link{pairwise.mahalanobis}} computes all
such pairwise Mahalanobis distances among groups and is useful for
quantifying the separation of groups in DA. Genetic sequences are composed
of discrete alphabetic characters, which makes estimates of variability
difficult. \code{\link{MolecularEntropy}} and \code{\link{MolecularMI}}
calculate the entropy and mutual information to estimate variability and
covariability, respectively, of DNA or Amino Acid sequences.  Functional
grouping of amino acids (Atchley et al 1999) is also available for entropy
and mutual information estimation.  Mutual information values can be
normalized by \code{\link{NMI}} to account for the background distribution
arising from the stochastic pairing of independent, random sites.
Alternatively, discrete alphabetic sequences can be transformed into
biologically informative metrics to be used in various multivariate
procedures.  \code{\link{FactorTransform}} converts amino acid sequences
using the amino acid indices determined by Atchley et al 2005.

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
%doc %{rlibdir}/HDMD/DESCRIPTION
%doc %{rlibdir}/HDMD/html
%{rlibdir}/HDMD/INDEX
%{rlibdir}/HDMD/Meta
%{rlibdir}/HDMD/R
%{rlibdir}/HDMD/NAMESPACE
%{rlibdir}/HDMD/help

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora