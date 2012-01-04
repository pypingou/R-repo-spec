%global packname  BaBooN
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Bayesian Bootstrap Predictive Mean Matching - Multiple and single imputation for discrete data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-nnet 

BuildRequires:    R-devel tex(latex) R-MASS R-nnet 

%description
The package contains two variants of Bayesian Bootstrap Predictive Mean
Matching to multiply impute missing data. The first variant is a
variable-by-variable imputation combining sequential regression and
Predictive Mean Matching (PMM) that has been extended for unordered
categorical data. The Bayesian Bootstrap allows for generating
approximately proper multiple imputations. The second variant is also
based on PMM, but the focus is on imputing several variables at the same
time. The suggestion is to use this variant, if the missing-data pattern
resembles a data fusion situation, or any other missing-by-design pattern,
where several variables have identical missing-data patterns. Both
variants can be run as 'single imputation' versions, in case the analysis
objective is of a purely descriptive nature.

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
%doc %{rlibdir}/BaBooN/DESCRIPTION
%doc %{rlibdir}/BaBooN/html
%{rlibdir}/BaBooN/R
%{rlibdir}/BaBooN/INDEX
%{rlibdir}/BaBooN/Meta
%{rlibdir}/BaBooN/NAMESPACE
%{rlibdir}/BaBooN/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora