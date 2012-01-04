%global packname  GEVcdn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          GEV conditonal density estimation network

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-VGAM 

BuildRequires:    R-devel tex(latex) R-VGAM 

%description
A flexible nonlinear modelling framework for nonstationary generalized
extreme value analysis in hydroclimatology

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
%doc %{rlibdir}/GEVcdn/html
%doc %{rlibdir}/GEVcdn/CITATION
%doc %{rlibdir}/GEVcdn/DESCRIPTION
%{rlibdir}/GEVcdn/help
%{rlibdir}/GEVcdn/Meta
%{rlibdir}/GEVcdn/R
%{rlibdir}/GEVcdn/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora