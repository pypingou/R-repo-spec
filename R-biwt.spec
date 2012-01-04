%global packname  biwt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Functions to compute the biweight mean vector and covariance & correlation matrices

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rrcov R-MASS 

BuildRequires:    R-devel tex(latex) R-rrcov R-MASS 

%description
Compute multivariate location, scale, and correlation estimates based on
Tukey's biweight M-estimator.

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
%doc %{rlibdir}/biwt/DESCRIPTION
%doc %{rlibdir}/biwt/html
%{rlibdir}/biwt/R
%{rlibdir}/biwt/NAMESPACE
%{rlibdir}/biwt/help
%{rlibdir}/biwt/INDEX
%{rlibdir}/biwt/Meta

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora