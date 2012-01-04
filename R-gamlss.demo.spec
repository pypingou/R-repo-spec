%global packname  gamlss.demo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.4
Release:          1%{?dist}
Summary:          Demos for GAMLSS

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rpanel R-gamlss R-gamlss.tr R-gamlss.util 

BuildRequires:    R-devel tex(latex) R-rpanel R-gamlss R-gamlss.tr R-gamlss.util 

%description
Demos for gamlss.family distributions.

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
%doc %{rlibdir}/gamlss.demo/html
%doc %{rlibdir}/gamlss.demo/DESCRIPTION
%{rlibdir}/gamlss.demo/INDEX
%{rlibdir}/gamlss.demo/help
%{rlibdir}/gamlss.demo/R
%{rlibdir}/gamlss.demo/NAMESPACE
%{rlibdir}/gamlss.demo/Meta

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.4-1
- initial package for Fedora