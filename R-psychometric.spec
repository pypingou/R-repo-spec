%global packname  psychometric
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Applied Psychometric Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-multilevel R-nlme 

BuildRequires:    R-devel tex(latex) R-multilevel R-nlme 

%description
Contains functions useful for correlation theory, meta-analysis
(validity-generalization), reliability, item analysis, inter-rater
reliability, and classical utility

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
%doc %{rlibdir}/psychometric/html
%doc %{rlibdir}/psychometric/DESCRIPTION
%{rlibdir}/psychometric/data
%{rlibdir}/psychometric/INDEX
%{rlibdir}/psychometric/NAMESPACE
%{rlibdir}/psychometric/help
%{rlibdir}/psychometric/R
%{rlibdir}/psychometric/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora