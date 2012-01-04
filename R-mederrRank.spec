%global packname  mederrRank
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Bayesian Methods for Identifying the Most Harmful Medication Errors

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-BB R-methods R-numDeriv R-utils 

BuildRequires:    R-devel tex(latex) R-BB R-methods R-numDeriv R-utils 

%description
This package implements two distinct but related statistical approaches to
the problem of identifying the combinations of medication error
characteristics that are more likely to result in harm: 1) Bayesian
hierarchical models with optimal Bayesian ranking on the log odds of harm,
and 2) an empirical Bayes model that estimates the ratio of the observed
count of harm to the count that would be expected if error characteristics
and harm were independent. In addition, for the Bayesian hierarchical
model, the package provides functions to assess the sensitivity of results
to different specifications of the random effects distributions.

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
%doc %{rlibdir}/mederrRank/DESCRIPTION
%doc %{rlibdir}/mederrRank/html
%{rlibdir}/mederrRank/R
%{rlibdir}/mederrRank/INDEX
%{rlibdir}/mederrRank/Meta
%{rlibdir}/mederrRank/data
%{rlibdir}/mederrRank/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora