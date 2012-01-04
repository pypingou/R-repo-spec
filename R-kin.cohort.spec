%global packname  kin.cohort
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Analysis of kin-cohort studies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Analysis of kin-cohort studies. kin.cohort provides estimates of
age-specific cumulative risk of a disease for carriers and noncarriers of
a mutation. The cohorts are retrospectively built from relatives of
probands for whom the genotype is known. Currently the method of moments
and marginal maximum likelihood are implemented. Confidence intervals are
calculated from bootstrap samples. Most of the code is a translation from
previous matlab code by Chatterjee.

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
%doc %{rlibdir}/kin.cohort/html
%doc %{rlibdir}/kin.cohort/DESCRIPTION
%{rlibdir}/kin.cohort/Meta
%{rlibdir}/kin.cohort/WishList
%{rlibdir}/kin.cohort/INDEX
%{rlibdir}/kin.cohort/ChangeLog
%{rlibdir}/kin.cohort/NAMESPACE
%{rlibdir}/kin.cohort/help
%{rlibdir}/kin.cohort/data
%{rlibdir}/kin.cohort/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora