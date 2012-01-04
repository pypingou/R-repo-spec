%global packname  DiagTest3Grp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Diagnostic test summary measures for three ordinal groups

Group:            Applications/Engineering 
License:          GPL (>= 3.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-car R-KernSmooth R-stats R-gplots 


BuildRequires:    R-devel tex(latex) R-car R-KernSmooth R-stats R-gplots



%description
Assuming diagnostic marker increase monotonically and stochatically with
disease severity, the R package provides utilities to estimate two
diagnostic test summary measures for three ordinal groups ----volume under
ROC surface (VUS) and the extended Youden index. Variance, confidence
interval and optimal cut-points both under the normal assumption and also
the non-parametric method(s) will be provided for the summary measures.
Statistical tests are implemented to compare multiple diagnostic tests and
two diagnostic test. Sample size is calculated to estimate the summary
measures within user-specified margin of error for future study planning.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora