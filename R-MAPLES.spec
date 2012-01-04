%global packname  MAPLES
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Smoothed age profile estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mgcv 

BuildRequires:    R-devel tex(latex) R-mgcv 

%description
MAPLES is a general method for the estimation of age profiles that uses
standard micro-level demographic survey data. The aim is to estimate
smoothed age profiles and relative risks for time-fixed and time-varying

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
%doc %{rlibdir}/MAPLES/html
%doc %{rlibdir}/MAPLES/DESCRIPTION
%{rlibdir}/MAPLES/INDEX
%{rlibdir}/MAPLES/help
%{rlibdir}/MAPLES/Meta
%{rlibdir}/MAPLES/data
%{rlibdir}/MAPLES/NAMESPACE
%{rlibdir}/MAPLES/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora