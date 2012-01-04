%global packname  nlmeODE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Non-linear mixed-effects modelling in nlme using differential equations

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-odesolve R-nlme R-lattice 

BuildRequires:    R-devel tex(latex) R-odesolve R-nlme R-lattice 

%description
This package combines the odesolve and nlme packages for mixed-effects
modelling using differential equations.

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
%doc %{rlibdir}/nlmeODE/DESCRIPTION
%doc %{rlibdir}/nlmeODE/html
%{rlibdir}/nlmeODE/R
%{rlibdir}/nlmeODE/help
%{rlibdir}/nlmeODE/INDEX
%{rlibdir}/nlmeODE/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora