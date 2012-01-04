%global packname  epibasix
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Elementary Epidemiological Functions for a Graduate Epidemiology\Biostatistics Course

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains elementary tools for analysis of common
epidemiological problems, ranging from sample size estimation, through 2x2
contingency table analysis and basic measures of agreement (kappa,
sensitivity/specificity). Appropriate print and summary statements are
also written to facilitate interpretation wherever possible.  This package
is a work in progress, so any comments or suggestions would be
appreciated.  Source code is commented throughout to facilitate
modification.  The target audience includes graduate students in various
epi/biostatistics courses.

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
%doc %{rlibdir}/epibasix/html
%doc %{rlibdir}/epibasix/DESCRIPTION
%{rlibdir}/epibasix/NAMESPACE
%{rlibdir}/epibasix/help
%{rlibdir}/epibasix/Meta
%{rlibdir}/epibasix/INDEX
%{rlibdir}/epibasix/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora