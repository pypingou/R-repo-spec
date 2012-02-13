%global packname  MatrixEQTL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{dist}
Summary:          Matrix eQTL: Ultra fast eQTL analysis via large matrix operations

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Matrix eQTL is designed for fast eQTL analysis on large datasets.  Matrix
eQTL can test for association between genotype and gene expression using
both linear regression and ANOVA models.  The models can include
covariates to account for such factors as population structure, gender,
and clinical variables.  It also supports models with heteroscedastic
and/or correlated errors, false discovery rate estimation and separate
treatment of local (cis) and distant (trans) eQTLs.

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
%doc %{rlibdir}/MatrixEQTL/DESCRIPTION
%doc %{rlibdir}/MatrixEQTL/html
%{rlibdir}/MatrixEQTL/NAMESPACE
%{rlibdir}/MatrixEQTL/help
%{rlibdir}/MatrixEQTL/R
%{rlibdir}/MatrixEQTL/INDEX
%{rlibdir}/MatrixEQTL/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- Update to version 1.5.0

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora