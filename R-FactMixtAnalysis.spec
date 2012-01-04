%global packname  FactMixtAnalysis
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Factor Mixture Analysis with covariates

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm 

%description
The package estimates Factor Mixture Analysis via the EM algorithm

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
%doc %{rlibdir}/FactMixtAnalysis/DESCRIPTION
%doc %{rlibdir}/FactMixtAnalysis/html
%{rlibdir}/FactMixtAnalysis/help
%{rlibdir}/FactMixtAnalysis/Meta
%{rlibdir}/FactMixtAnalysis/R
%{rlibdir}/FactMixtAnalysis/INDEX
%{rlibdir}/FactMixtAnalysis/NAMESPACE

%changelog
* Tue Dec 06 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora