%global packname  icaOcularCorrection
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Independent Components Analysis (ICA) based eye-movement correction.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fastICA 

BuildRequires:    R-devel tex(latex) R-fastICA 

%description
Removes eye-movements artifacts as well as (a portion of) of other noise
using the fastICA package. The correction methods is based on Flexer,
Bauer, Pripfl, and Dorffner (2005).

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
%doc %{rlibdir}/icaOcularCorrection/NEWS
%doc %{rlibdir}/icaOcularCorrection/DESCRIPTION
%doc %{rlibdir}/icaOcularCorrection/html
%{rlibdir}/icaOcularCorrection/R
%{rlibdir}/icaOcularCorrection/Meta
%{rlibdir}/icaOcularCorrection/data
%{rlibdir}/icaOcularCorrection/INDEX
%{rlibdir}/icaOcularCorrection/help
%{rlibdir}/icaOcularCorrection/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora