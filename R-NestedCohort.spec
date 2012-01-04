%global packname  NestedCohort
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Survival Analysis for Cohorts with Missing Covariate Information

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-MASS 

BuildRequires:    R-devel tex(latex) R-survival R-MASS 

%description
Estimate hazard ratios, survival curves and attributable risks for cohorts
with missing covariates, using Cox models or Kaplan-Meier estimated for
strata.  This handles studies nested within cohorts, such as case-cohort
studies with stratified sampling.  See

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
%doc %{rlibdir}/NestedCohort/doc
%doc %{rlibdir}/NestedCohort/html
%doc %{rlibdir}/NestedCohort/DESCRIPTION
%{rlibdir}/NestedCohort/data
%{rlibdir}/NestedCohort/R
%{rlibdir}/NestedCohort/NAMESPACE
%{rlibdir}/NestedCohort/help
%{rlibdir}/NestedCohort/INDEX
%{rlibdir}/NestedCohort/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora