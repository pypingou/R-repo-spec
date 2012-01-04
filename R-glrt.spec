%global packname  glrt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Generalized Logrank Tests for Interval-censored Failure Time Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-survival R-splines R-Icens 

BuildRequires:    R-devel tex(latex) R-stats R-survival R-splines R-Icens 

%description
Functions to conduct three generalized logrank tests and a score test
under a proportional hazards model

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
%doc %{rlibdir}/glrt/DESCRIPTION
%doc %{rlibdir}/glrt/html
%{rlibdir}/glrt/data
%{rlibdir}/glrt/Meta
%{rlibdir}/glrt/R
%{rlibdir}/glrt/help
%{rlibdir}/glrt/INDEX
%{rlibdir}/glrt/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora