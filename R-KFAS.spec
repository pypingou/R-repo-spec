%global packname  KFAS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Kalman filter and smoothers for exponential family state space models.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Package KFAS provides functions for Kalman filtering, state, disturbance
and simulation smoothing, forecasting and simulation of state space
models. All functions can use exact diffuse initialisation when
distributions of some or all elements of initial state vector are unknown.
Filtering, state smoothing and simulation functions use sequential
processing algorithm, which is faster than standard approach, and it also
allows singularity of prediction error variance matrix. KFAS also contains
function for computing the likelihood of exponential family state space
models and function for state smoothing of exponential family state space

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
%doc %{rlibdir}/KFAS/DESCRIPTION
%doc %{rlibdir}/KFAS/html
%{rlibdir}/KFAS/R
%{rlibdir}/KFAS/help
%{rlibdir}/KFAS/INDEX
%{rlibdir}/KFAS/NAMESPACE
%{rlibdir}/KFAS/libs
%{rlibdir}/KFAS/data
%{rlibdir}/KFAS/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1-1
- initial package for Fedora