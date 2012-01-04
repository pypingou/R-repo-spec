%global packname  BayHaz
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          R Functions for Bayesian Hazard Rate Estimation

Group:            Applications/Engineering 
License:          GPL Version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-splines 

%description
A suite of R functions for Bayesian estimation of smooth hazard rates via
Compound Poisson Process (CPP) and Bayesian Penalized Spline (BPS) priors.

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
%doc %{rlibdir}/BayHaz/DESCRIPTION
%doc %{rlibdir}/BayHaz/html
%{rlibdir}/BayHaz/INDEX
%{rlibdir}/BayHaz/Meta
%{rlibdir}/BayHaz/help
%{rlibdir}/BayHaz/NAMESPACE
%{rlibdir}/BayHaz/R
%{rlibdir}/BayHaz/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora