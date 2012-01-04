%global packname  CDM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Cognitive Diagnosis Modeling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Functions and example empirical (i.e., fraction subtraction) and
artificial data for cognitive diagnosis modeling.  This package implements
parameter estimation procedures for the deterministic-input,
noisy-and-gate (DINA) and deterministic-input, noisy-or-gate (DINO) models
and procedures for analyzing data under these models.  See package?CDM for
an overview.

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
%doc %{rlibdir}/CDM/DESCRIPTION
%doc %{rlibdir}/CDM/COPYING
%doc %{rlibdir}/CDM/html
%{rlibdir}/CDM/NAMESPACE
%{rlibdir}/CDM/Meta
%{rlibdir}/CDM/R
%{rlibdir}/CDM/help
%{rlibdir}/CDM/INDEX
%{rlibdir}/CDM/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora