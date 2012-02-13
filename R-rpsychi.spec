%global packname  rpsychi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{dist}
Summary:          Statistics for psychiatric research

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) R-gtools 

%description
The rpsychi offers a number of functions for psychiatry, psychiatric
nursing, clinical psychology. Functions are primarily for statistical
significance testing using published work. For example, you can conduct a
factorial analysis of variance (ANOVA), which requires only the mean,
standard deviation, and sample size for each cell, rather than the
individual data. This package covers fundamental statistical tests such as
t-test, chi-square test, analysis of variance, and multiple regression
analysis. With some exceptions, you can obtain effect size and its
confidence interval. These functions help you to obtain effect size from
published work, and then to conduct a priori power analysis or
meta-analysis, even if a researcher do not report effect size in a
published work.

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
%doc %{rlibdir}/rpsychi/html
%doc %{rlibdir}/rpsychi/NEWS
%doc %{rlibdir}/rpsychi/DESCRIPTION
%{rlibdir}/rpsychi/NAMESPACE
%{rlibdir}/rpsychi/INDEX
%{rlibdir}/rpsychi/Meta
%{rlibdir}/rpsychi/help
%{rlibdir}/rpsychi/R

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- Update to version 0.8

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora