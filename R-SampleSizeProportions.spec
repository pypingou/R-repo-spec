%global packname  SampleSizeProportions
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Calculating sample size requirements when estimating the difference between two binomial proportions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A set of R functions for calculating sample size requirements using three
different Bayesian criteria in the context of designing an experiment to
estimate the difference between two binomial proportions. Functions for
calculation of required sample sizes for the Average Length Criterion, the
Average Coverage Criterion and the Worst Outcome Criterion in the context
of binomial observations are provided. In all cases, estimation of the
difference between two binomial proportions is considered. Functions for
both the fully Bayesian and the mixed Bayesian/likelihood approaches are

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
%doc %{rlibdir}/SampleSizeProportions/html
%doc %{rlibdir}/SampleSizeProportions/DESCRIPTION
%{rlibdir}/SampleSizeProportions/INDEX
%{rlibdir}/SampleSizeProportions/help
%{rlibdir}/SampleSizeProportions/Meta
%{rlibdir}/SampleSizeProportions/NAMESPACE
%{rlibdir}/SampleSizeProportions/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora