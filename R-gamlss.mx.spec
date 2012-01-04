%global packname  gamlss.mx
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.4
Release:          1%{?dist}
Summary:          A GAMLSS add on package for fitting mixture distributions

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gamlss R-nnet R-MASS 

BuildRequires:    R-devel tex(latex) R-gamlss R-nnet R-MASS 

%description
The main purpose of this package is to allow fitting of mixture
distributions with GAMLSS models.

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
%doc %{rlibdir}/gamlss.mx/html
%doc %{rlibdir}/gamlss.mx/DESCRIPTION
%{rlibdir}/gamlss.mx/INDEX
%{rlibdir}/gamlss.mx/help
%{rlibdir}/gamlss.mx/data
%{rlibdir}/gamlss.mx/NAMESPACE
%{rlibdir}/gamlss.mx/R
%{rlibdir}/gamlss.mx/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.4-1
- initial package for Fedora