%global packname  ssize.fdr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Sample Size Calculations for Microarray Experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains a set of functions that calculates appropriate
sample sizes for one-sample t-tests, two-sample t-tests, and F-tests for
microarray experiments based on desired power while controlling for false
discovery rates. For all tests, the standard deviations (variances) among
genes can be assumed fixed or random. This is also true for effect sizes
among genes in one-sample and two sample experiments. Functions also
output a chart of power versus sample size, a table of power at different
sample sizes, and a table of critical test values at different sample

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
%doc %{rlibdir}/ssize.fdr/html
%doc %{rlibdir}/ssize.fdr/DESCRIPTION
%{rlibdir}/ssize.fdr/help
%{rlibdir}/ssize.fdr/Meta
%{rlibdir}/ssize.fdr/NAMESPACE
%{rlibdir}/ssize.fdr/INDEX
%{rlibdir}/ssize.fdr/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora