%global packname  nltm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Non-linear Transformation Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Fits a non-linear transformation model (nltm) for analyzing survival data,
see Tsodikov (2003) "Semiparametricmodels: a generalized self-consistency
approach". J.R. Statistical Society B, 65, Part 3, 759-774. The class of
nltm includes the following currently supported models: Cox proportional
hazard, proportional hazard cure, proportional odds, proportional hazard -
proportional hazard cure, proportional hazard - proportional odds cure,
Gamma frailty, and proportional hazard - proportional odds.

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
%doc %{rlibdir}/nltm/DESCRIPTION
%doc %{rlibdir}/nltm/html
%{rlibdir}/nltm/libs
%{rlibdir}/nltm/data
/usr/lib/debug/.build-id/71/d08f91193b521021083aa73af829523c1c859a
/usr/src/debug/nltm/nltm/src/dmat.cc
%{rlibdir}/nltm/Meta
/usr/src/debug/nltm/nltm/src/models.cc
/usr/src/debug/nltm/nltm/src/profileLik.cc
%{rlibdir}/nltm/R
/usr/lib/debug/.build-id/71/d08f91193b521021083aa73af829523c1c859a.debug
%{rlibdir}/nltm/help
/usr/src/debug/nltm/nltm/src/covariance.cc
%{rlibdir}/nltm/INDEX
/usr/src/debug/nltm/nltm/src/printVector.cc
%{rlibdir}/nltm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora