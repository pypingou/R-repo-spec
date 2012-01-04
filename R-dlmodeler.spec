%global packname  dlmodeler
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Generalized Dynamic Linear Modeler

Group:            Applications/Engineering 
License:          GPL (>= 2) | BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
dlmodeler is a set of user-friendly functions to simplify the state-space
modelling, fitting, analysis and forecasting of Generalized Dynamic Linear
Models (DLMs). It includes functions to name and extract individual
components of a DLM, build classical seasonal time-series models (monthly,
quarterly, yearly, etc. with calendar adjustments) and provides a unified
interface compatible with other state-space packages including: dlm, FKF
and KFAS.

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
%doc %{rlibdir}/dlmodeler/html
%doc %{rlibdir}/dlmodeler/DESCRIPTION
%{rlibdir}/dlmodeler/help
%{rlibdir}/dlmodeler/Meta
%{rlibdir}/dlmodeler/NAMESPACE
%{rlibdir}/dlmodeler/INDEX
%{rlibdir}/dlmodeler/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora