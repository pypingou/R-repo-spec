%global packname  simexaft
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          simexaft

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-survival R-mvtnorm 

%description
Implement of the Simulation-Extrapolation (SIMEX) algorithm for the
accelerated failure time (AFT) with covariates subject to measurement

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
%doc %{rlibdir}/simexaft/html
%doc %{rlibdir}/simexaft/DESCRIPTION
%{rlibdir}/simexaft/Meta
%{rlibdir}/simexaft/R
%{rlibdir}/simexaft/data
%{rlibdir}/simexaft/help
%{rlibdir}/simexaft/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora