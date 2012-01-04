%global packname  rmeta
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.16
Release:          1%{?dist}
Summary:          Meta-analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
Functions for simple fixed and random effects meta-analysis for two-sample
comparisons and cumulative meta-analyses. Draws standard summary plots,
funnel plots, and computes summaries and tests for association and

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
%doc %{rlibdir}/rmeta/DESCRIPTION
%doc %{rlibdir}/rmeta/html
%{rlibdir}/rmeta/help
%{rlibdir}/rmeta/Meta
%{rlibdir}/rmeta/data
%{rlibdir}/rmeta/R
%{rlibdir}/rmeta/NAMESPACE
%{rlibdir}/rmeta/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.16-1
- initial package for Fedora