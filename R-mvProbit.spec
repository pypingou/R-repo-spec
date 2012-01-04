%global packname  mvProbit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Multivariate Probit Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-maxLik R-abind 
Requires:         R-bayesm R-miscTools 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-maxLik R-abind
BuildRequires:    R-bayesm R-miscTools 


%description
Tools for multivariate probit models

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
%doc %{rlibdir}/mvProbit/DESCRIPTION
%doc %{rlibdir}/mvProbit/html
%{rlibdir}/mvProbit/INDEX
%{rlibdir}/mvProbit/R
%{rlibdir}/mvProbit/NAMESPACE
%{rlibdir}/mvProbit/help
%{rlibdir}/mvProbit/Meta

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora