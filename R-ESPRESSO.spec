%global packname  ESPRESSO
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{dist}
Summary:          Power Analysis and Sample Size Calculation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
The package allows for the Estimation of Sample-size and Power by
Exploring Simulated Study Outcomes. It supports simulation-based power
calculation for stand-alone case-control studies and for case-control
analyses nested in cohort studies, that take account of realistic
assessment error.

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
%doc %{rlibdir}/ESPRESSO/DESCRIPTION
%doc %{rlibdir}/ESPRESSO/html
%{rlibdir}/ESPRESSO/NAMESPACE
%{rlibdir}/ESPRESSO/data
%{rlibdir}/ESPRESSO/INDEX
%{rlibdir}/ESPRESSO/R
%{rlibdir}/ESPRESSO/help
%{rlibdir}/ESPRESSO/Meta

%changelog
* Mon Feb 13 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- Update to version 1.1

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora