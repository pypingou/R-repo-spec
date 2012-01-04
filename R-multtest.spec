%global packname  multtest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.10.0
Release:          1%{?dist}
Summary:          Resampling-based multiple hypothesis testing

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase 

%description
Non-parametric bootstrap and permutation resampling-based multiple testing
procedures (including empirical Bayes methods) for controlling the
family-wise error rate (FWER), generalized family-wise error rate (gFWER),
tail probability of the proportion of false positives (TPPFP), and false
discovery rate (FDR).  Several choices of bootstrap-based null
distribution are implemented (centered, centered and scaled,
quantile-transformed). Single-step and step-wise methods are available.
Tests based on a variety of t- and F-statistics (including t-statistics
based on regression parameters from linear and survival models as well as
those based on correlation parameters) are included.  When probing
hypotheses with t-statistics, users may also select a potentially faster
null distribution which is multivariate normal with mean zero and variance
covariance matrix derived from the vector influence function.  Results are
reported in terms of adjusted p-values, confidence regions and test
statistic cutoffs. The procedures are directly applicable to identifying
differentially expressed genes in DNA microarray experiments.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.10.0-1
- initial package for Fedora