%global packname  GlobalAncova
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.22.0
Release:          1%{?dist}
Summary:          Calculates a global test for differential gene expression between groups

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-corpcor R-globaltest 

BuildRequires:    R-devel tex(latex) R-methods R-corpcor R-globaltest 

%description
We give the following arguments in support of the GlobalAncova approach:
After appropriate normalisation, gene-expression-data appear rather
symmetrical and outliers are no real problem, so least squares should be
rather robust. ANCOVA with interaction yields saturated data modelling
e.g. different means per group and gene. Covariate adjustment can help to
correct for possible selection bias. Variance homogeneity and uncorrelated
residuals cannot be expected. Application of ordinary least squares gives
unbiased, but no longer optimal estimates (Gauss-Markov-Aitken).
Therefore, using the classical F-test is inappropriate, due to
correlation. The test statistic however mirrors deviations from the null
hypothesis. In combination with a permutation approach, empirical
significance levels can be approximated. Alternatively, an approximation
yields asymptotic p-values. This work was supported by the NGFN grant 01
GR 0459, BMBF, Germany.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.22.0-1
- initial package for Fedora