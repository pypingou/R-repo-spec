%global packname  ivivc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          A data analysis tool for in vitro-in vivo correlation (IVIVC)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats4 R-rgenoud R-odesolve R-reshape R-sciplot 


BuildRequires:    R-devel tex(latex) R-stats4 R-rgenoud R-odesolve R-reshape R-sciplot



%description
a menu-driven package for IVIVC model buidling and model validation

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
%changelog
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora