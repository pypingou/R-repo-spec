%global packname  gamlss.nl
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.5
Release:          1%{?dist}
Summary:          Fitting non linear parametric GAMLSS models

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gamlss R-survival 

BuildRequires:    R-devel tex(latex) R-gamlss R-survival 

%description
This is an add on package to GAMLSS. It allows one extra method for
fitting GAMLSS models. The main function nlgamlss() can fit any parametric
(up to four parameter) GAMLSS distribution.

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
%doc %{rlibdir}/gamlss.nl/DESCRIPTION
%doc %{rlibdir}/gamlss.nl/html
%{rlibdir}/gamlss.nl/R
%{rlibdir}/gamlss.nl/INDEX
%{rlibdir}/gamlss.nl/NAMESPACE
%{rlibdir}/gamlss.nl/help
%{rlibdir}/gamlss.nl/Meta
%{rlibdir}/gamlss.nl/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.5-1
- initial package for Fedora