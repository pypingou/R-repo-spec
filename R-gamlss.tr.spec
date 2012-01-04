%global packname  gamlss.tr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.4
Release:          1%{?dist}
Summary:          Generating and fitting truncated (gamlss.family) distributions

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gamlss 

BuildRequires:    R-devel tex(latex) R-gamlss 

%description
This is an add on package to GAMLSS. The purpose of this package is to
allow users to defined truncated distributions in GAMLSS models. The main
function gen.trun() generates truncated version of an existing GAMLSS
family distribution.

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
%doc %{rlibdir}/gamlss.tr/DESCRIPTION
%doc %{rlibdir}/gamlss.tr/html
%{rlibdir}/gamlss.tr/INDEX
%{rlibdir}/gamlss.tr/Meta
%{rlibdir}/gamlss.tr/R
%{rlibdir}/gamlss.tr/help
%{rlibdir}/gamlss.tr/NAMESPACE

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.4-1
- initial package for Fedora