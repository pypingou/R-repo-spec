%global packname  dynCorr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Dynamic Correlation Package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpridge 

BuildRequires:    R-devel tex(latex) R-lpridge 

%description
Computes dynamical correlation estimates and percentile bootstrap
confidence intervals for pairs of longitudinal responses, including
consideration of lags and derivatives.

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
%doc %{rlibdir}/dynCorr/DESCRIPTION
%doc %{rlibdir}/dynCorr/html
%{rlibdir}/dynCorr/R
%{rlibdir}/dynCorr/INDEX
%{rlibdir}/dynCorr/help
%{rlibdir}/dynCorr/data
%{rlibdir}/dynCorr/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora