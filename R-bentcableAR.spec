%global packname  bentcableAR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Bent-Cable Regression for Independent Data or Autoregressive Time Series

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains two main interfaces for fitting and diagnosing
bent-cable regressions for autoregressive time-series data or independent
data (time series or otherwise). The interfaces are 'bentcable.ar()' and
'bentcable.dev.plot()'. Some components in the package can also be used as
stand-alone functions. The bent cable (linear-quadratic-linear)
generalizes the broken stick (linear-linear), which is also handled by
this package. Version 0.2 corrects a glitch in the computation of
confidence intervals for the CTP. References updated from Versions 0.2.1
and 0.2.2 appear in Version 0.2.3.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora