%global packname  smatr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2.4
Release:          1%{dist}
Summary:          (Standardised) Major Axis Estimation and Testing Routines

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides methods of fitting bivariate lines in allometry
using the major axis (MA) or standardised major axis (SMA), and for making
inferences about such lines. The available methods of inference include
confidence intervals and one-sample tests for slope and elevation, testing
for a common slope or elevation amongst several allometric lines,
constructing a confidence interval for a common slope or elevation, and
testing for no shift along a common axis, amongst several samples.

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
%doc %{rlibdir}/smatr/DESCRIPTION
%doc %{rlibdir}/smatr/html
%{rlibdir}/smatr/Meta
%{rlibdir}/smatr/NAMESPACE
%{rlibdir}/smatr/help
%{rlibdir}/smatr/data
%{rlibdir}/smatr/INDEX
%{rlibdir}/smatr/R

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.4-1
- Update to version 3.2.4

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.3-1
- initial package for Fedora